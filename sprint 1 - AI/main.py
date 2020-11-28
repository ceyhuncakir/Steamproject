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

    # De functie hier onder aangepast met min 1, nu is die het zelfde als die hier boven maar flexibel! Yes/No?
    #if counter > (len(obj) - 1):
    #    counter = 0

    return item


inladen()

# print('niet', steam[0])
# print('niet', steam[1])
# sort('release_date', 1)
# print(steam[0]['release_date'])
# print(steam[1]['release_date'])
# print(steam[2]['release_date'])
# print(steam[3]['release_date'])
# sort("negative_ratings", 1)
# print(steam[0]["negative_ratings"])
# print(steam[1]["negative_ratings"])
# print(steam[2]["negative_ratings"])
# print(steam[3]["negative_ratings"])
#
# print("hier", sortnext("negative_ratings", 0))