import json

steam = {}


def inladen():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: item})  # data[counter] verandert naar item. het doet de zelfde handeling.
            counter += 1


def sort(dictionary, str):
    temp = {}
    for item in dictionary:
        try:
            temp[dictionary[item][str]] = temp[dictionary[item][str]] + [item]
        except:
            temp[dictionary[item][str]] = [item]
    temp2 = sorted(temp)
    temp3 = {}
    for item in temp2:
        temp3[item] = temp[item]
    temp2 = {}
    counter = 0
    for group in temp3:
        for item in temp3[group]:
            temp2[counter] = dictionary[item]
            counter += 1
    return temp2

inladen()
sortdev = sort(steam, "developer")
print(sortdev[1])
print(steam[0])