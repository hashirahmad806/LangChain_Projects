from langchain.tools import tool
from langchain_nimble import NimbleSearchTool
from dotenv import load_dotenv
import os

# Request pakacge is used to make HTTP requests to the weather API to get the weather data for a specific city.
import requests
load_dotenv()


SearchTool = NimbleSearchTool(
    # k means the number of results to return from the search, default is 5
    k=5,
    deep_search=True,  # deep search will return more relevant results, default is False
    # parsing type can be either "markdown" or "html", default is "markdown"
    parsing_type="markdown"
)


@tool
def google_search(query: str):
    """
    Search anything on the Google for realtime information .

    Args:
        query (str): The query to user search for google search.

    Returns:
            The search results from Google.
    """
    res = SearchTool.invoke(query)
    return res


@tool
def weather_search(city: str):
    """
        Get Real  time weather  details like temperature, humidity, wind speed, and more for a specific city.
    Args:
        city ---> city name for which you want to get the weather information.

    Returns:
            Weather data from the api response.

    """
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    res = requests.get(API_URL)
    if res.status_code != 200:
        return f"Error: Unable to fetch weather data for {city}. Please check the city name and try again."
    if res.status_code == 200:
        return res.json()

    return f"Error: Unable to fetch weather data for {city}. Please check the city name and try again."


ALL_TOOLS = [google_search, weather_search]
