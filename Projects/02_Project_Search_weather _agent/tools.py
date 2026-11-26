from langchain_nimble import NimbleSearchTool

from langchain.tools import tool

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
    res = SearchTool.invoke(f"Weather in {city}")
    return res


ALL_TOOLS = [google_search, weather_search]
