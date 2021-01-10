import json
from random import randint

class StartupApiTi:
    def __init__(self):
        self.steam2 = []
        self.steam_cath = []
        self.counter = 0

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
    def give_name(self):
        my_json_file = open('./data/steam.json', 'r')
        jsondata = my_json_file.read()
        obj = json.loads(jsondata)
        item = str(obj[self.counter]["name"])
        self.counter += 1
        if self.counter > (len(obj) - 1):
            self.counter = 0
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

class node:

    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:

    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self.insert_value(value, self.root)

    def insert_value(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child == node(value)
            else:
                self.insert_value(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child == node(value)
            else:
                self.insert_value(value, current_node.right_child)
        else:
            print("die waarde zit al in de tree")

    def print_tree(self):
        if self.root != None:
            self.print_value(self.root)

    def print_value(self, current_node):
        if current_node != None:
            self.print_value(current_node.left_child)
            print(str(current_node.value))
            self.print_value(current_node.right_child)

    def height(self):
        if self.root != None:
            return self.get_height(self.root, 0)
        else:
            return 0

    def get_height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self.get_height(current_node.left_child, current_height + 1)
        right_height = self.get_height(current_node.right_child, current_height + 1)

        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self.search_values(value, self.root)
        else:
            return False

    def search_values(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self.search_values(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self.search_values(value, current_node.right_child)
        return False

def fill_tree(tree, num_elems=200, max_int=1000):
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

Startup = StartupApiTi()
Startup.inladen()
sort_func = SortingAlgorithms(Startup.steam2, Startup.steam_cath)
calc_statistiek = Statistiek(Startup.steam2, Startup.steam_cath)

tree = binary_search_tree() # initialiseert de tree
tree = fill_tree(tree) # vult automatisch de tree
#tree.insert(8) # kunnen handmatig de tree vullen met values
#tree.search(5) # kunnen op een bepaalde value kijken of de value in de tree bestaat zoja geeft het een true statement terug zo niet dan een false statement
tree.print_tree() # print de hele tree met de hoogte van de tree
print("boom hoogte: " + str(tree.height()))

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
