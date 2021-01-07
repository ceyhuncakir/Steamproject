import json

# (het werkt nog niet met de Gui)
steam2 = []
steam_cath = []
def inladen2():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        # Categorien worden apart opgeslagen
        temp = []
        for cath in data[0].keys():
            temp.append(cath)
        steam_cath.append(tuple(temp))
        # Categorien word gescheiden van de data voorkomt nuttelose data, (zou anders ook geen logies indeling weten)
        load_counter = 0
        for item in data:
            temp_tuple = ()
            for value_item in item.values():
                tem = (value_item,)
                temp_tuple = temp_tuple + tem
            steam2.append(temp_tuple)
            load_counter += 1
    # Hier onder voorbeeld van uitkomst de steam_cath zall worden gebruikt door de gui
    # en steam is alle data van elke game in een lijst met tuples
    print(steam_cath)
    print(steam2[0])
inladen2()

# inplaats van de sorted function (het werkt nog niet met de Gui)



def basic_sort(str):
    sort_on = steam_cath[0].index(str)
    # Hier moet iets komen om te bepalen of op nummer of string of date gesorteerd gaat worden
    # hier onder een insertion sort voor getallen.
    sorted_steam = steam2.copy()
    for index in range(1, (len(sorted_steam))):
        copy_list = sorted_steam[index]
        index_grens = index
        print('something', index, len(sorted_steam)) # Hij doet het maar het duurt voor eeuwig als er veel verandert.
        while sorted_steam[index_grens][sort_on] < sorted_steam[index_grens - 1][sort_on] and index_grens > 0:
            sorted_steam[index_grens] = sorted_steam[index_grens - 1]
            sorted_steam[index_grens - 1] = copy_list
            index_grens -= 1
    # return sorted_steam
    print(type(sorted_steam[0][2]))
    print(sorted_steam[0][1], 'basic_sort')
    print(sorted_steam[0][0], 'basic_sort')
    print(sorted_steam[1][1], 'basic_sort')
    print(sorted_steam[1][0], 'basic_sort')
    print(sorted_steam[2][1], 'basic_sort')
    print(sorted_steam[2][0], 'basic_sort')
    print(sorted_steam[3][1], 'basic_sort')
    print(sorted_steam[3][0], 'basic_sort')
    print(sorted_steam[4][1], 'basic_sort')
    print(sorted_steam[4][0], 'basic_sort')

# Als er niets verandert hoeft te worden 3 seconden
basic_sort('appid')
# Als er veel moet veranderen duurt het voor eeuwig (betere simple sort zoeken??)
# basic_sort('price')
# basic_sort('name')



steam = {}
def inladen():
    with open('./Data/steam.json', 'r') as steamdata:
        data = json.load(steamdata)
        counter = 0
        for item in data:
            steam.update({counter: item})  # data[counter] verandert naar item. het doet de zelfde handeling.
            counter += 1


def sort(str, OGK):
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
    return steam


#  Deze gaan we niet gebruiken (Klopt niet met opdrachten canvas)
# sortstorage = ["appid",0,0]
# def sortnext(searchterm, OGK):
#     global sortstorage
#     if OGK == None:
#         OGK = 0
#     sortstorage[2] += 1
#     if sortstorage[2] == 27064:
#         sortstorage[2] = 0
#     if sortstorage != [searchterm, OGK, sortstorage[2]]:
#         sortstorage = [searchterm, OGK, 0]
#         sort(searchterm, OGK)
#     return str(steam[sortstorage[2]]['name'])


counter = 0
def give_name():
    my_json_file = open('./data/steam.json', 'r')
    jsondata = my_json_file.read()
    obj = json.loads(jsondata)
    global counter
    item = str(obj[counter]["name"])
    counter += 1
    if counter > (len(obj) - 1):
        counter = 0
    return item

