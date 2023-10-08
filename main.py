# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def print_hi(name):
    API_URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            # The request was successful
            data = response.json()  # Parse the JSON response
            print(data)
        else:
            # Handle errors
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
