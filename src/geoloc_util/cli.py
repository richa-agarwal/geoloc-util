import argparse
from geoloc_util.geo_location_utility import GeoLocationUtility


def main():
    parser = argparse.ArgumentParser(
        description="Geolocation Utility\n"
                    "--------------------\n"
                    "This utility provides geographical information for given locations.\n Examples:\n geoloc-util "
                    "\"Madison, WI\" \"12345\" \n geoloc-util \"Madison, WI\" \"Chicago, IL\" \"10001\"",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "locations",
        nargs="+",
        help="List of locations (city, state or zip code).Examples- City and state: \"Madison, WI\"\n - Zip code: "
             "\"12345\"",
    )
    args = parser.parse_args()

    results = GeoLocationUtility.process_locations(args.locations)

    for result in results:
        if "error" in result:
            print(result["error"])
        else:
            print(f"Location: {result['name']}{',' + result['state'] if result['state'] != 'N/A' else '' }, "
                  f"{result['country']}")
            print(f"Latitude: {result['lat']}")
            print(f"Longitude: {result['lon']}")
        print()


if __name__ == "__main__":
    main()
