#! python3

import config
import re
import requests

hit_dice_regex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')

api = config.apiKey
req_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": api,
        "n": 0,
        "min": 1,
        "max": 0,
        "replacement": True,
        "base": 10
    },
    "id": 18730
}


def parse_dice(dice_to_parse):
    rolls = hit_dice_regex.findall(dice_to_parse.lower())
    nums = []
    dice = []
    for roll in rolls:
        if 'd' in roll:
            die = roll.split('d')
            if die[0] in ('', '+', '-'):
                die[0] = die[0] + '1'
            dice.append(list(map(int, die)))
        else:
            nums.append(int(roll))
    nums.extend(roll_dice(dice))
    return sum(nums)


def roll_dice(rand_list):
    results = []
    for i in rand_list:
        req_data['params']['n'] = i[0]
        req_data['params']['max'] = i[1]
        response = requests.post('https://api.random.org/json-rpc/1/invoke', json=req_data)
        response.raise_for_status()
        json = response.json()
        data = json['result']['random']['data']
        results.extend(data)
    return results


print(parse_dice(input('Roll the dice!\n')))
