#! python3

import requests

reqData = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "00000000-0000-0000-0000-000000000000",
        "n": 0,
        "min": 1,
        "max": 0,
        "replacement": True,
        "base": 10
    },
    "id": 18730
}