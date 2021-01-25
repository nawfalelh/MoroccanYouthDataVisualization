import requests, json

def extract_data():
    from hcp_meta_data import sources

    for s in sources:
        try:
            response = requests.get(s['url'])
            data = response.json()
            filename = './lake/hcp/hcp_data_{}.json'.format(s['name'])
            with open(filename, 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except requests.RequestException:
            print('Unable to get {}'.format(s['url']))