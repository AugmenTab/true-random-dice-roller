#! python3

from collections import namedtuple
from itertools import groupby
import config
import re
import requests


def parse_die(roll):
    Roll = namedtuple('Roll', 'n max')
    x = roll.split('d')
    die = Roll(x[0], x[1])
    if die.n in ('', '+', '-'):
        die.n = die.n + '1'
        print(die)
    return die


def parse_dice(dice_to_parse):
    hit_dice_regex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')
    rolls = hit_dice_regex.findall(dice_to_parse.lower())
    groups = groupby(rolls, lambda r: 'dice' if 'd' in r else 'modifier')
    parsers = {'dice': parse_die, 'modifier': int}
    return {k: list(map(lambda a: parsers[k](a), g)) for k, g in groups}


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
    parsed_dice = parse_dice(user_input)
    result = sum(parsed_dice.get('modifier', [])) + sum(roll_dice(parsed_dice.get('dice', []), req_data))
    print(result)


if __name__ == '__main__':
    main()
