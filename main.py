# This is a sample Python script.
import csv

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from pprint import pprint


def transform_to_csv(file: object) -> None:
    header = ['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation']
    data = [
        ['01000US', 'United States', '2020', '2020', '326569308', 'united-states']
    ]

    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(data)


def print_hi(name):
    API_URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            # The request was successful
            file = open("usa_population.json", "w")
            # file.write(response.text)
            transform_to_csv(file)
            file.close()
            # pprint(response.text)
        else:
            # Handle errors
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
