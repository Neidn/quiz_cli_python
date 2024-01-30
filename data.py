import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

url = "https://opentdb.com/api.php"


def get_data():
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = get_data()
