import pytest
from geoloc_util.geo_location_utility import GeoLocationUtility


class TestGeoLocationUtility:

    @pytest.mark.parametrize("location, expected_keys", [
        ("New York, NY", ["name", "state", "country", "lat", "lon"]),
        ("Los Angeles, CA", ["name", "state", "country", "lat", "lon"]),
        ("Chicago, IL", ["name", "state", "country", "lat", "lon"]),
    ])
    def test_valid_city_state(self, location, expected_keys):
        result = GeoLocationUtility.get_location_by_name(location)
        assert all(key in result for key in expected_keys)
        assert result["name"] in location
        assert result["country"] == "US"

    @pytest.mark.parametrize("zipcode, expected_name", [
        ("10001", "New York"),
        ("90210", "Beverly Hills"),
        ("60601", "Chicago"),
    ])
    def test_valid_zipcode(self, zipcode, expected_name):
        result = GeoLocationUtility.get_location_by_zip(zipcode)
        assert "name" in result
        assert result["name"] == expected_name
        assert result["country"] == "US"
        assert "lat" in result and "lon" in result

    def test_invalid_city_state(self):
        result = GeoLocationUtility.get_location_by_name("InvalidCity, XX")
        assert "error" in result
        assert "No results found" in result["error"]

    def test_invalid_zipcode(self):
        result = GeoLocationUtility.get_location_by_zip("00000")
        assert "error" in result

    @pytest.mark.parametrize("locations", [
        (["New York, NY", "90210", "Chicago, IL"]),
        (["10001", "Los Angeles, CA", "60601"]),
    ])
    def test_multiple_locations(self, locations):
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        assert all("name" in result for result in results if "error" not in result)

    def test_empty_input(self):
        result = GeoLocationUtility.process_locations([])
        assert len(result) == 0

    @pytest.mark.parametrize("location", [
        "New York, NY",
        "90210",
        "Chicago, IL",
        "InvalidCity, XX",
        "00000",
    ])
    def test_api_response_time(self, location):
        import time
        start_time = time.time()
        GeoLocationUtility.get_location_data(location)
        end_time = time.time()
        assert end_time - start_time < 5  # Assuming a 5-second timeout

    @pytest.mark.parametrize("locations, expected_names", [
        (
                ["New York, NY", "90210", "Chicago, IL", "75001", "San Francisco, CA"],
                ["New York", "Beverly Hills", "Chicago", "Carrollton", "San Francisco"]
        ),
        (
                ["10001", "Los Angeles, CA", "60601", "Houston, TX", "20001"],
                ["New York", "Los Angeles", "Chicago", "Houston", "Washington"]
        ),
    ])
    def test_mixed_locations(self, locations, expected_names):
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        for result, expected_name in zip(results, expected_names):
            if "error" not in result:
                assert result["name"] == expected_name
            else:
                print(f"Error for input: {result['error']}")

    def test_all_invalid_locations(self):
        locations = ["InvalidCity, XX", "00000", "NonexistentTown, YY", "99999"]
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        assert all("error" in result for result in results)

    def test_mixed_valid_and_invalid_locations(self):
        locations = ["New York, NY", "00000", "Chicago, IL", "InvalidCity, XX", "90210"]
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        valid_results = [result for result in results if "error" not in result]
        invalid_results = [result for result in results if "error" in result]
        assert len(valid_results) == 3  # New York, Chicago, and Beverly Hills
        assert len(invalid_results) == 2  # 00000 and InvalidCity

    def test_duplicate_locations(self):
        locations = ["New York, NY", "10001", "New York, NY", "10001"]
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        assert all(result["name"] == "New York" for result in results if "error" not in result)

    def test_case_insensitivity(self):
        locations = ["new york, ny", "CHICAGO, il", "los angeles, ca"]
        results = GeoLocationUtility.process_locations(locations)
        assert len(results) == len(locations)
        assert all("error" not in result for result in results)
        assert [result["name"] for result in results] == ["New York", "Chicago", "Los Angeles"]

    @pytest.mark.parametrize("location", [
        "",  # Empty string
        "   ",  # Whitespace only
        ",",  # Just a comma
        "12",  # Incomplete zipcode
        "A, B",  # Too short for city, state
        "12345677",  # Invalid length zip code
    ])
    def test_edge_case_inputs(self, location):
        result = GeoLocationUtility.get_location_data(location)
        assert "error" in result
