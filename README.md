# Geolocation Utility

This utility provides geographical information for given locations using the OpenWeatherMap API.

## Installation

You can install this package directly from the GitHub repository:
```
pip install git+https://github.com/richa-agarwal/geoloc-util.git
```

For development:

1. Clone this repository:
```
git clone https://github.com/richa-agarwal/geoloc-util.git 
cd geoloc-util
```

2. Install the package in editable mode:
```
pip install -e .
```


## Usage

After installation, you can use the geoloc-util from the command line to get location information for cities, states, or zip codes.

Basic usage:
```
geoloc-util [LOCATIONS...]
```

Examples:
```
geoloc-util "New York, NY" 90210 geoloc_util "Chicago, IL" "Los Angeles, CA" 75001
```

The utility accepts any number of locations, which can be a mix of city/state combinations and zip codes.

## Running Tests

To run the tests, ensure you have pytest installed (it's included in the requirements.txt), then run:

```
pytest tests/test_geoloc_util.py
```

This will run all the integration tests, which include:
- Testing valid city/state and zip code inputs
- Testing invalid inputs
- Testing mixed inputs (city/state and zip codes)
- Testing edge cases and error handling

Note: These tests make actual API calls, so ensure you have a stable internet connection and be mindful of API rate limits.

## API Key

This utility uses the OpenWeatherMap API. 
The API key is currently hardcoded in the `config.py` file. 
For security reasons, in a production environment, you should use environment variables or a secure configuration management system to handle the API key.

