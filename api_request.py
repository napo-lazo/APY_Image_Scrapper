import requests

def makeRequest(data):

    r = requests.get(data['url'], headers=data['headers'])

    if r.status_code == 200:
        print("success in api request")
        j = r.json()
        return j
    else:
        print(f"failure: {r.status_code} - {r.reason}")