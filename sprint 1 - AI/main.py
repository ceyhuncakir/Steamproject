import json
steam = {}


def inladen():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: item})  # data[counter] verandert naar item. het doet de zelfde handeling.
            counter += 1

#testing
inladen()
print(steam[0])
print(steam[1])
