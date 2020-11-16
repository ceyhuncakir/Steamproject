import json

steam = {}


def inladen():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: item})  # data[counter] verandert naar item. het doet de zelfde handeling.
            counter += 1


def sort(dictionary, str, OGK):
    if OGK == None:
        OGK = 0
    temp = {}
    for item in dictionary:
        try:
            temp[dictionary[item][str]] = temp[dictionary[item][str]] + [item]
        except:
            temp[dictionary[item][str]] = [item]
    temp2 = sorted(temp, reverse=OGK)
    temp3 = {}
    counter = 0
    for group in temp2:
        for item in temp[group]:
            temp3[counter] = dictionary[item]
            counter += 1
    return temp3


def sort_name():
    my_json_file = open('./data/steam.json', 'r')
    jsondata = my_json_file.read()
    obj = json.loads(jsondata)
    item = str(obj[0]["name"])

    return item



inladen()
sortdev = sort(steam, "positive_ratings", 1)
print(sortdev)
print(steam[0])