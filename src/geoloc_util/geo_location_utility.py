
from geoloc_util.api_client import APIClient


class GeoLocationUtility:

    @staticmethod
    def get_location_data(location: str) -> dict:
        if location.replace(" ", "").isdigit():
            return GeoLocationUtility.get_location_by_zip(location)
        else:
            return GeoLocationUtility.get_location_by_name(location)

    @staticmethod
    def get_location_by_name(location: str) -> dict:
        data = APIClient.get_location_by_name(location)

        if not data:
            return {"error": f"No results found for {location}"}

        result = data[0]
        return GeoLocationUtility.process_result(result)

    @staticmethod
    def get_location_by_zip(zipcode: str) -> dict:
        data = APIClient.get_location_by_zip(zipcode)

        return GeoLocationUtility.process_result(data)

    @staticmethod
    def process_result(result: dict):
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
        return [GeoLocationUtility.get_location_data(location) for location in locations]
