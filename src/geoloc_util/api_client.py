import requests
from geoloc_util.config import API_KEY, BASE_URL, COUNTRY_CODE


class APIClient:
    """
    A client for interacting with the OpenWeatherMap Geocoding API.

    This class provides static methods to fetch location data by name or zip code.
    """
    @staticmethod
    def get_location_by_name(location: str) -> dict:
        """
        Fetch location data by city name from the OpenWeatherMap API.

        Args:
            location (str): The name of the location to look up.

        Returns:
            dict: A dictionary containing the API response data. If an error occurs,
                  it returns a list with a single dictionary containing an error message.

        Raises:
            No exceptions are raised; errors are caught and returned in the result.
        """
        url = f"{BASE_URL}direct"
        params = {
            "q": f"{location}, {COUNTRY_CODE}",
            "limit": 1,
            "appid": API_KEY
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            print(err)
            return [{"error": f"Error for location \"{location}\""}]

    @staticmethod
    def get_location_by_zip(zipcode: str) -> dict:
        """
        Fetch location data by zip code from the OpenWeatherMap API.

        Args:
            zipcode (str): The zip code to look up.

        Returns:
            dict: A dictionary containing the API response data. If an error occurs,
                  it returns a dictionary with an error message.

        Raises:
            No exceptions are raised; errors are caught and returned in the result.
        """
        url = f"{BASE_URL}zip"
        params = {
            "zip": f"{zipcode},{COUNTRY_CODE}",
            "appid": API_KEY
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            return {"error": f"Error for zipcode \"{zipcode}\""}
