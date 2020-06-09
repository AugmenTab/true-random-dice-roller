#! python3

import re #, requests

hitDiceRegex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')

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

def rollDice(diceToRoll):
    rolls = hitDiceRegex.findall(diceToRoll.lower())
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
    nums.extend(getRandom(dice))
    #return sum(nums)

def getRandom(params):
    print(params)

#response = requests.post('https://api.random.org/json-rpc/1/invoke', json = reqData)
#response.raise_for_status()
#json = response.json()
#data = json['result']['random']['data']
#print(data)

print(rollDice(input('Roll the dice!\n')))