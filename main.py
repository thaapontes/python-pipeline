# This is a sample Python script.
import csv

import requests
from pprint import pprint

from requests import Response

# Functional way: use a Map (format -> function)
available_formats = ['csv', 'json', 'parquet']


# OOO way: create a class for each format


def transform_to_csv(response: Response, file_format):
    response_data = response.json()
    header = response_data['data'][0].keys()
    data = []

    for row in response_data['data']:
        values = [row[key] for key in header]
        data.append(values)

    with open(f'{file_format}_file', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        for row in data:
            writer.writerow(row)


# TODO create unit tests
def transform_to_required_format(response: Response, file_format: str) -> None:
    if file_format == 'csv':
        transform_to_csv(response, file_format)
    elif file_format == 'json':
        with open(f'{file_format}_file', 'w', encoding='UTF8') as file:
            writer = file.write(response.text)


def print_hi(name):
    API_URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            # The request was successful
            file_format = 'csv'
            transform_to_required_format(response, file_format)
        else:
            # Handle errors
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
