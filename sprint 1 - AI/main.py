import json


class StartupApiTi:
    def __init__(self):
        self.steam2 = []
        self.steam_cath = []

    def inladen(self):
        with open('./Data/steam.json', 'r') as steamdata:
            data = json.load(steamdata)
            # Categorien worden apart opgeslagen
            temp = []
            for cath in data[0].keys():
                temp.append(cath)
            self.steam_cath.append(tuple(temp))
            # Categorien word gescheiden van de data voorkomt nuttelose data, (zou anders ook geen logies indeling weten)
            load_counter = 0
            for item in data:
                temp_tuple = ()
                for value_item in item.values():
                    tem = (value_item,)
                    temp_tuple = temp_tuple + tem
                self.steam2.append(temp_tuple)
                load_counter += 1
        # Hier onder voorbeeld van uitkomst de steam_cath die zal worden gebruikt door de gui
        # en steam2 is alle data van elke game in een lijst met tuples
        print(self.steam_cath)
        # steam_cath = [('appid', 'name', 'release_date', ... )]
        print(self.steam2[0])
        # steam2 =  [(10, 'Counter-Strike', '2000-11-01', ... ), (20, 'Team Fortress Classic', '1999-04-01',... ), ...]

    # Geen idee in welke classe name func
    counter = 0
    def give_name(self):
        my_json_file = open('./data/steam.json', 'r')
        jsondata = my_json_file.read()
        obj = json.loads(jsondata)
        global counter
        item = str(obj[counter]["name"])
        counter += 1
        if counter > (len(obj) - 1):
            counter = 0
        return item


class SortingAlgorithms:
    def __init__(self, list_1, list_2):
        self.steam2 = list_1
        self.steam_cath = list_2

    # inplaats van de sorted function (het werkt nog niet met de Gui)
    # "Niet haalbaar voor een 6 minuten filmpje"
    def basic_sort(self, cath):
        print("start basic_sort")
        sort_on = self.steam_cath[0].index(cath)
        # hier onder een insertion sort.
        sorted_steam = self.steam2.copy()
        for index in range(1, (len(sorted_steam))):
            copy_list = sorted_steam[index]
            index_grens = index
            # print('something', index, len(sorted_steam)) # Hij doet het maar het duurt voor eeuwig als er veel verandert.
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


class Statistiek:
    def __init__(self, list_1, list_2):
        self.steam2 = list_1
        self.steam_cath = list_2

    def get_relevante_data(self, given_list, index_location):
        # Zorgt dat alle relevante data bij elkaar wordt gehaald. (Voorkomt complicaties bij andere functies)
        # Anders worden bepaalde functies ook herhaald bij bijvoorbeeld centrum en spreidings maten uitrekenen
        relevante_list = [self.steam_cath[0][index_location]]
        for item in given_list:
            relevante_list.append(item[index_location])
        # Voorbeeld: ['price', 7.19, 3.99, 3.99, 3.99,]
        return relevante_list

    def gemiddelde(self, relevant_list):
        amount = 0
        for index in range(1, len(relevant_list)):  # Van af 1 vanwege tag
            amount += relevant_list[index]
        gemidelde = amount / (len(relevant_list) - 1)
        print(int(gemidelde), "gemiddelt aantal", relevant_list[0])
        return gemidelde

    def rnge(self, relevant_list):
        high = max(relevant_list[1:])
        low = min(relevant_list[1:])
        range_uitkomst = high - low
        print(int(range_uitkomst), "range van", relevant_list[0])
        return range_uitkomst

    def median(self, relevant_list):
        lenght_list = (len(relevant_list) - 1)  # -1 vanwege de tag
        midden_punt = lenght_list // 2
        if lenght_list % 2 == 0:
            mediaan = ((relevant_list[midden_punt] + relevant_list[midden_punt - 1]) / 2)
        else:
            mediaan = relevant_list[midden_punt + 1]  # Tag
        print(mediaan, "median")
        return mediaan

    def variantie(self, relevant_list):
        var_gemidelde = self.gemiddelde(relevant_list)
        resultaat = 0
        for index in range(1, len(relevant_list)):
            afwijking = relevant_list[index] - var_gemidelde
            resultaat += afwijking * afwijking
        var = resultaat / len(self.steam2)
        print(int(var), "variantie van", relevant_list[0])
        return var

    def standaard_def(self, relevant_list):
        var_list = self.variantie(relevant_list)
        antwoord = var_list ** (1 / 2)
        print(int(antwoord), "standaarddeviatie van", relevant_list[0])
        return antwoord

    def kwartiel_gen(self, relevant_list):
        kwartiel_null = relevant_list[1]  # Een tag in de lijst van daar niet 0
        middenpunt = (len(relevant_list) - 1) // 2
        kwartiel_een = self.median(relevant_list[:middenpunt])
        kwartiel_twee = relevant_list[middenpunt]
        if (len(relevant_list) - 1) % 2 == 0:  # -1 vanwege de tag in de lijst
            kwartiel_drie = self.median(relevant_list[middenpunt - 1:])  # omgedraait vanwege tag (median haalt er 1 af)
        else:
            kwartiel_drie = self.median(relevant_list[middenpunt:])
        kwartiel_vier = relevant_list[-1]
        iqr = kwartiel_drie - kwartiel_een
        print('Kwartiel 0 t/m 4 en iqr', kwartiel_null, kwartiel_een, kwartiel_twee, kwartiel_drie, kwartiel_vier, iqr)
        return kwartiel_null, kwartiel_een, kwartiel_twee, kwartiel_drie, kwartiel_vier, iqr


Startup = StartupApiTi()
Startup.inladen()
sort_func = SortingAlgorithms(Startup.steam2, Startup.steam_cath)
calc_statistiek = Statistiek(Startup.steam2, Startup.steam_cath)

# Testing uikomst
# calc_statistiek.gemiddelde(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.rnge(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.median(calc_statistiek.get_relevante_data(sort_func.basic_sort('price'), 17))
# calc_statistiek.variantie(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.standaard_def(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.kwartiel_gen(calc_statistiek.get_relevante_data(sort_func.basic_sort('price'), 17))


# Hier Onder Tijdelijke backup oude functies tot bevestiging van joost over vraag

# def rnge(index_location):
#     rnge_list = steam2.copy()
#     higest = rnge_list[0][index_location]
#     lowest = rnge_list[0][index_location]
#     for index in range(0, (len(rnge_list)) - 1):
#         if higest < rnge_list[index][index_location]:
#             higest = rnge_list[index][index_location]
#         if lowest > rnge_list[index][index_location]:
#             lowest = rnge_list[index][index_location]
#     range_uitkomst = higest - lowest
#     print(int(range_uitkomst), "range van", steam_cath[0][index_location])
#     return range_uitkomst

# def median(index_location):
#     sort_list = basic_sort(steam_cath[0][index_location])
#     lenght_list = len(sort_list)
#     midden_punt = lenght_list//2
#     if lenght_list % 2 == 0:
#         mediaan = ((sort_list[midden_punt][index_location] + sort_list[midden_punt-1][index_location]) / 2)
#     else:
#         mediaan = sort_list[midden_punt][index_location]
#     print(mediaan, "median van", steam_cath[0][index_location])

# def variantie(index_location):
#     var_gemidelde = gemidelde(index_location)
#     resultaat = 0
#     for item in steam2:
#         afwijking = item[index_location] - var_gemidelde
#         resultaat += afwijking * afwijking
#     var = resultaat / len(steam2)
#     print(int(var), "variantie van", steam_cath[0][index_location])
#     return var

# def interkwartiel_sub(list_num):
#     lenghte_list = len(list_num)
#     midden_punt = lenghte_list // 2
#     if lenghte_list % 2 == 0:
#         mediaan = ((list_num[midden_punt] + list_num[midden_punt-1]) / 2)
#     else:
#         mediaan = list_num[midden_punt]
#     return mediaan
#
#
# def interkwatiel(index_location):
#     sort_list = basic_sort(steam_cath[0][index_location])
#     lenghte_list = len(sort_list)
#     midden_punt = lenghte_list // 2
#     q1 = interkwartiel_sub(sort_list[:midden_punt])
#     if len(sort_list) % 2 == 0:
#         q3 = interkwartiel_sub(sort_list[midden_punt:])
#     else:
#         q3 = interkwartiel_sub(sort_list[midden_punt + 1:])
#     ikr = q3 - q1
#     print(int(ikr), "interkwatiel van", steam_cath[0][index_location])