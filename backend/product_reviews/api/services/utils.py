import re
import os
import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def check_alpha_exists(data):
    """
        1.Checks whether the data contains atleast one alphabet or not.
        2. Returns the value based on expression.
    """
    logger.info(" Checking Alphabet Existence..")
    return_value = re.search('[a-zA-Z]', data)
    logger.info(" Returned value is : " + str(return_value))
    return return_value


def check_positivenum(data):
    """
        1. Checks whether the data is Positive Number or not.
        2. Logs returned value into log file.
    """
    logger.info(" Checking Positive Number..")
    return_value = len(re.findall(r'^[0-9]+$', str(data)))
    logger.info(" Returned value is : " + str(return_value))
    return return_value


def get_countries():
    """
        Get the list of countries and its cities
    """
    file_path = os.path.join(os.getcwd(), 'fixtures/countries_cities.json')
    json_data = json.load(open(file_path, 'r'))
    countries = []
    cities = []
    for key, values in json_data.items():
        countries.append((key.lower(), key.upper()))
        for val in values:
            cities.append((val.lower(), val.upper()))
    return tuple(countries), tuple(cities)


def check_city_exists(country, city):
    """
        Checks whether the specified city exists in selected country or not.
    """
    file_path = os.path.join(os.getcwd(), 'fixtures/countries_cities.json')
    json_data = json.load(open(file_path, 'r'))
    for key, values in json_data.items():
        if (key.lower() == country.lower() and any(
                city.lower() == val.lower() for val in values)):
            return True
    return False
