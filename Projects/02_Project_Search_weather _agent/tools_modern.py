import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from langchain.tools import tool
from tools import google_search


WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def _get_json(url: str, params: dict) -> dict:
    request_url = f"{url}?{urlencode(params)}"
    request = Request(request_url, headers={"User-Agent": "weather-search-agent/1.0"})
    with urlopen(request, timeout=15) as response:
        return json.load(response)


def _display_unit(unit: str) -> str:
    return {
        "°C": "degrees Celsius",
        "°F": "degrees Fahrenheit",
    }.get(unit, unit)


@tool
def weather_search(city: str) -> str:
    """Get current weather conditions for a city."""
    city = city.strip()
    if not city:
        raise ValueError("Provide a city name to look up current weather.")

    location_data = _get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        {"name": city, "count": 1, "language": "en", "format": "json"},
    )
    locations = location_data.get("results", [])
    if not locations:
        raise ValueError(f"No matching location was found for '{city}'.")

    location = locations[0]
    forecast = _get_json(
        "https://api.open-meteo.com/v1/forecast",
        {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": (
                "temperature_2m,relative_humidity_2m,apparent_temperature,"
                "precipitation,weather_code,wind_speed_10m"
            ),
            "timezone": "auto",
        },
    )
    current = forecast.get("current")
    if not current:
        raise RuntimeError(f"The weather service returned no current data for '{city}'.")

    current_units = forecast.get("current_units", {})
    location_name = ", ".join(
        part
        for part in (location.get("name"), location.get("admin1"), location.get("country"))
        if part
    )
    weather_code = current.get("weather_code")
    condition = WEATHER_CODES.get(weather_code, f"Unknown weather code ({weather_code})")
    timezone = forecast.get("timezone", "local time")

    return (
        f"Current weather for {location_name} "
        f"({current.get('time', 'time unavailable')} {timezone}):\n"
        f"- Conditions: {condition}\n"
        f"- Temperature: {current['temperature_2m']} "
        f"{_display_unit(current_units.get('temperature_2m', ''))}\n"
        f"- Feels like: {current['apparent_temperature']} "
        f"{_display_unit(current_units.get('apparent_temperature', ''))}\n"
        f"- Humidity: {current['relative_humidity_2m']} "
        f"{current_units.get('relative_humidity_2m', '')}\n"
        f"- Precipitation: {current['precipitation']} "
        f"{current_units.get('precipitation', '')}\n"
        f"- Wind speed: {current['wind_speed_10m']} "
        f"{current_units.get('wind_speed_10m', '')}\n"
        "Source: Open-Meteo current conditions (weather-model data)."
    )


ALL_TOOLS = [google_search, weather_search]
