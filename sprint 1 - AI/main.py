import json
steam = {}


def inladen():
    with open('steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: data[counter]})
            counter += 1


