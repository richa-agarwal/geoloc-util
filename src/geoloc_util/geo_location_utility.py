from geoloc_util.api_client import APIClient


class GeoLocationUtility:
    """
    A utility class for retrieving and processing geographical location data.
    """

    @staticmethod
    def get_location_data(location: str) -> dict:
        """
        Determine the type of location input and retrieve corresponding geographical data.

        Args:
            location (str): A string representing either a city name or a zip code.

        Returns:
            dict: A dictionary containing geographical data for the given location.
        """
        if location.replace(" ", "").isdigit():
            return GeoLocationUtility.get_location_by_zip(location)
        else:
            return GeoLocationUtility.get_location_by_name(location)

    @staticmethod
    def get_location_by_name(location: str) -> dict:
        """
        Retrieve geographical data for a given location name.

        Args:
            location (str): A string representing a city name.

        Returns:
            dict: A dictionary containing geographical data for the given location name.
                  Returns an error message if no results are found.
        """
        data = APIClient.get_location_by_name(location)

        if not data:
            return {"error": f"No results found for {location}"}

        result = data[0]
        return GeoLocationUtility.process_result(result)

    @staticmethod
    def get_location_by_zip(zipcode: str) -> dict:
        """
        Retrieve geographical data for a given zip code.

        Args:
            zipcode (str): A string representing a zip code.

        Returns:
            dict: A dictionary containing geographical data for the given zip code.
        """
        data = APIClient.get_location_by_zip(zipcode)

        return GeoLocationUtility.process_result(data)

    @staticmethod
    def process_result(result: dict) -> dict:
        """
        Process the raw result from the API into a standardized format.

        Args:
            result (dict): A dictionary containing raw geographical data.

        Returns:
            dict: A dictionary containing processed geographical data in a standardized format.
                  Returns the original result if it contains an error.
        """
        if "error" in result:
            return result
        return {
            "name": result["name"],
            "state": result.get("state", "N/A"),
            "country": result["country"],
            "lat": result["lat"],
            "lon": result["lon"]
        }

    @staticmethod
    def process_locations(locations: list[str]) -> list[dict]:
        """
        Process multiple locations and retrieve their geographical data.

        Args:
            locations (list[str]): A list of strings, each representing a location (city name or zip code).

        Returns:
            list[dict]: A list of dictionaries, each containing geographical data for a location.
        """
        return [GeoLocationUtility.get_location_data(location) for location in locations]
