#! python3

import config
import re, requests

hitDiceRegex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')

api = config.apiKey
reqData = {
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

def parseDice(diceToParse):
    rolls = hitDiceRegex.findall(diceToParse.lower())
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
    nums.extend(rollDice(dice))
    return sum(nums)

def rollDice(randList):
    results = []
    for i in randList:
        reqData['params']['n'] = i[0]
        reqData['params']['max'] = i[1]
        response = requests.post('https://api.random.org/json-rpc/1/invoke', json = reqData)
        response.raise_for_status()
        json = response.json()
        data = json['result']['random']['data']
        results.extend(data)
    return results

print(parseDice(input('Roll the dice!\n')))