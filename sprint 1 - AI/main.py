import json

steam = {}


def inladen():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: item})  # data[counter] verandert naar item. het doet de zelfde handeling.
            counter += 1


def sort(str, OGK):
    global steam
    if OGK == None:
        OGK = 0
    temp = {}
    for item in steam:
        if temp.get(steam[item][str]) != None:
            temp[steam[item][str]] = temp[steam[item][str]] + [item]
        else:
            temp[steam[item][str]] = [item]
    temp2 = sorted(temp, reverse=OGK)
    temp3 = {}
    counter = 0
    for group in temp2:
        for item in temp[group]:
            temp3[counter] = steam[item]
            counter += 1
    steam = temp3
    return steam

counter = 0
def give_name():
    my_json_file = open('./data/steam.json', 'r')
    jsondata = my_json_file.read()
    obj = json.loads(jsondata)
    global counter
    item = str(obj[counter]["name"])
    counter += 1
    return item



inladen()
sort("positive_ratings", 1)