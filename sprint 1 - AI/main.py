import json

steam = {}
sortstorage = ["appid",0,0]

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
    count = 0
    for group in temp2:
        for item in temp[group]:
            temp3[count] = steam[item]
            count += 1
    steam = temp3
    return steam

def sortnext(searchterm, OGK):
    global sortstorage
    if OGK == None:
        OGK = 0
    sortstorage[2] += 1
    if sortstorage[2] == 27064:
        sortstorage[2] = 0
    if sortstorage != [searchterm, OGK, sortstorage[2]]:
        sortstorage = [searchterm, OGK, 0]
        sort(searchterm, OGK)
    return str(steam[sortstorage[2]]['name'])


counter = 0
def give_name():
    my_json_file = open('./data/steam.json', 'r')
    jsondata = my_json_file.read()
    obj = json.loads(jsondata)
    global counter
    item = str(obj[counter]["name"])
    counter += 1
    if counter > 27063:
        counter = 0
    #if counter > len(obj):
    #    counter = 0

    return item



inladen()
sort("positive_ratings", 1)