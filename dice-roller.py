#! python3

from collections import namedtuple
import config
import re
import requests


def parse_dice(dice_to_parse, req_data):
    hit_dice_regex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')
    rolls = hit_dice_regex.findall(dice_to_parse.lower())
    nums = []
    dice = []
    for roll in rolls:
        if 'd' in roll:
            Roll = namedtuple('Roll', 'n max')
            x = roll.split('d')
            die = Roll(x[0], x[1])
            if die.n in ('', '+', '-'):
                die.n = die.n + '1'
            dice.append(die)
        else:
            nums.append(int(roll))
    nums.extend(roll_dice(dice, req_data))
    return sum(nums)


def roll_dice(rand_list, req_data):
    results = []
    for i in rand_list:
        req_data['params']['n'] = i.n
        req_data['params']['max'] = i.max
        response = requests.post('https://api.random.org/json-rpc/1/invoke', json=req_data)
        response.raise_for_status()
        json = response.json()
        data = json['result']['random']['data']
        results.extend(data)
    return results


def main():
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
    user_input = input('Roll the dice!\n')
    result = parse_dice(user_input, req_data)
    print(result)


if __name__ == '__main__':
    main()
