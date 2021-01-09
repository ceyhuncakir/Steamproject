import json

# Het werkt nog niet met de Gui
# Er is of iets fout met hoe de data structuur nu wordt ingeladen of de basic sort moet anders
# Voor bijvoorbeeld het uit rekenen van het mediaan of variantie die een gesorteerde lijst nodig heeft duur het eeuwig.
# "Niet haalbaar voor een 6 minuten filmpje"
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
    # Hier onder voorbeeld van uitkomst de steam_cath die zal worden gebruikt door de gui
    # en steam2 is alle data van elke game in een lijst met tuples
    print(steam_cath)
    # steam_cath = [('appid', 'name', 'release_date', ... )]
    print(steam2[0])
    # steam2 =  [(10, 'Counter-Strike', '2000-11-01', ... ), (20, 'Team Fortress Classic', '1999-04-01',... ), ...]
inladen2()

# inplaats van de sorted function (het werkt nog niet met de Gui)
def basic_sort(str):
    sort_on = steam_cath[0].index(str)
    # hier onder een insertion sort.
    sorted_steam = steam2.copy()
    for index in range(1, (len(sorted_steam))):
        copy_list = sorted_steam[index]
        index_grens = index
        print('something', index, len(sorted_steam)) # Hij doet het maar het duurt voor eeuwig als er veel verandert.
        while sorted_steam[index_grens][sort_on] < sorted_steam[index_grens - 1][sort_on] and index_grens > 0:
            sorted_steam[index_grens] = sorted_steam[index_grens - 1]
            sorted_steam[index_grens - 1] = copy_list
            index_grens -= 1
    return sorted_steam

# Als er niets verandert hoeft te worden 3 seconden
# basic_sort('appid')
# Als er veel moet veranderen duurt het voor eeuwig (betere simple sort zoeken? of ligt het aan de indeling data)
# basic_sort('price')
# basic_sort('name')
# basic_sort('positive_ratings')

def gemidelde(index_location):
    list_gemiddelde = steam2.copy()
    amount = 0
    for index in range(0, (len(list_gemiddelde)) - 1):
        amount += list_gemiddelde[index][index_location]
    gemidelde = amount / len(list_gemiddelde)
    print(int(gemidelde), "gemiddelt aantal", steam_cath[0][index_location])
    return gemidelde


gemidelde(12)
gemidelde(17)


def rnge(index_location):
    rnge_list = steam2.copy()
    higest = rnge_list[0][index_location]
    lowest = rnge_list[0][index_location]
    for index in range(0, (len(rnge_list)) - 1):
        if higest < rnge_list[index][index_location]:
            higest = rnge_list[index][index_location]
        if lowest > rnge_list[index][index_location]:
            lowest = rnge_list[index][index_location]
    range_uitkomst = higest - lowest
    print(int(range_uitkomst), "range van", steam_cath[0][index_location])
    return range_uitkomst


rnge(17)


def median(index_location):
    sort_list = basic_sort(steam_cath[0][index_location])
    lenght_list = len(sort_list)
    midden_punt = lenght_list//2
    if lenght_list % 2 == 0:
        mediaan = ((sort_list[midden_punt][index_location] + sort_list[midden_punt-1][index_location]) / 2)
    else:
        mediaan = sort_list[midden_punt][index_location]
    print(mediaan, "median van", steam_cath[0][index_location])
# median(17)


def variantie(index_location):
    var_gemidelde = gemidelde(index_location)
    resultaat = 0
    for item in steam2:
        afwijking = item[index_location] - var_gemidelde
        resultaat += afwijking * afwijking
    var = resultaat / len(steam2)
    print(int(var), "variantie van", steam_cath[0][index_location])
    return var


variantie(17)

def standaard_def(index_location):
    var_list = variantie(index_location)
    antwoord = var_list**(1/2)
    print(int(antwoord), "standaarddeviatie van", steam_cath[0][index_location])


standaard_def(17)

def interkwartiel_sub(list_num):
    lenghte_list = len(list_num)
    midden_punt = lenghte_list // 2
    if lenghte_list % 2 == 0:
        mediaan = ((list_num[midden_punt] + list_num[midden_punt-1]) / 2)
    else:
        mediaan = list_num[midden_punt]
    return mediaan


def interkwatiel(index_location):
    sort_list = basic_sort(steam_cath[0][index_location])
    lenghte_list = len(sort_list)
    midden_punt = lenghte_list // 2
    q1 = interkwartiel_sub(sort_list[:midden_punt])
    if len(sort_list) % 2 == 0:
        q3 = interkwartiel_sub(sort_list[midden_punt:])
    else:
        q3 = interkwartiel_sub(sort_list[midden_punt + 1:])
    ikr = q3 - q1
    print(int(ikr), "interkwatiel van", steam_cath[0][index_location])
# interkwatiel is nog niet af
# interkwatiel(17)

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

