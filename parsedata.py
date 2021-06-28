import requests

from stop_words import STOP_WORDS

def filterdata(data_user):
    filter_data = []
    for data in data_user.split():
        if data not in STOP_WORDS:
            filter_data.append(data)
    return filter_data


def geocoddde(address):
    data = []
    GOOGLE_MAPS_API_URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key='

    req = requests.get(GOOGLE_MAPS_API_URL)
    d = req.json()
    data.append(d)
    for datageo in data:
        print(data)


if __name__ == "__main__":
    geocoddde('Paris')
