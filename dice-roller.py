#! python3

import requests

reqData = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "00000000-0000-0000-0000-000000000000",
        "n": 10,
        "min": 1,
        "max": 10,
        "replacement": True,
        "base": 10
    },
    "id": 18730
}

response = requests.post('https://api.random.org/json-rpc/1/invoke', json = reqData)
response.raise_for_status()
json = response.json()
data = json['result']['random']['data']
print(data)