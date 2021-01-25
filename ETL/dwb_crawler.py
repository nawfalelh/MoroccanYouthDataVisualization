import requests, json
import pandas as pd

def extract_data():

    names_and_codes = pd.read_csv('./lake/dwb/dwb_names_and_codes.csv')

    series_codes = list(names_and_codes['Series Code'])

    url = 'http://api.worldbank.org/v2/country/mar/indicator/{}?per_page=100&format=json'

    for sc in series_codes:
        try:
            response = requests.get(url.format(sc))
            data = response.json()
            filename = './lake/dwb/data_{}.json'.format(sc)
            with open(filename, 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except requests.RequestException:
            print('Unable to get {}'.format(url.format(sc)))