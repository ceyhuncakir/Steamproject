import json
from random import randint

class StartupApiTi:
    def __init__(self):
        self.steam2 = []
        self.steam_cath = []
        self.counter = 0
        self.part_list = []
        self.max_size = 987  # limit Gui = 5000, limit recursion = 987.
        self.part_index = 0

    def split_list(self):
        # De data is te groot en wordt hier gesplit.
        for i in range(0, len(self.steam2), self.max_size):
            self.part_list.append(self.steam2[i:i + self.max_size])
            # part_list = [[(), (), ()...700], [(), (), ()...700], [(), (), ()...700],......]


    def inladen(self):
        with open('./Data/steam.json', 'r') as steamdata:
            data = json.load(steamdata)
            # Categorien worden apart opgeslagen
            temp = []
            for cath in data[0].keys():
                temp.append(cath)
            self.steam_cath.append(tuple(temp))
            # Categorien word gescheiden van de data voorkomt nuttelose data,
            load_counter = 0
            for item in data:
                temp_tuple = ()
                for value_item in item.values():
                    tem = (value_item,)
                    temp_tuple = temp_tuple + tem
                self.steam2.append(temp_tuple)
                load_counter += 1
        print(self.steam_cath)
        # steam_cath = [('appid', 'name', 'release_date', ... )]
        print(self.steam2[0])
        # steam2 =  [(10, 'Counter-Strike', '2000-11-01', ... ), (20, 'Team Fortress Classic', '1999-04-01',... ), ...]

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
    def __init__(self, list_2):
        self.steam_cath = list_2

    def basic_insertion(self, cath):
        print("start basic insertion sort")
        sort_on = self.steam_cath[0].index(cath)
        # sorted_steam = self.steam2.copy()
        sorted_steam = Startup.part_list[Startup.part_index]

        for index in range(1, (len(sorted_steam))): #traversed van 1 tot het lengte van het list met tuples
            copy_list = sorted_steam[index] #gesorteerd lijst met index aangegeven
            index_grens = index # variable voor het grens van het index
            while sorted_steam[index_grens][sort_on] < sorted_steam[index_grens - 1][sort_on] and index_grens > 0: #kijkt op de index grens waar het gesorteerd moet worden op de gesorteerd lijst dat word bekeken of het kleiner is dan de gesorteerd lijst met een index grens value van - 1 en er word gtekeken of index grens groter is dan 0
                sorted_steam[index_grens] = sorted_steam[index_grens - 1]
                sorted_steam[index_grens - 1] = copy_list
                index_grens -= 1 # hier word de grens met 1 elke keer vermindert
        return sorted_steam

    def basic_selection(self, cath):
        sort_on = self.steam_cath[0].index(cath) # variable voor het categorie
        # sorted_steam = self.steam2.copy()
        sorted_steam = Startup.part_list[Startup.part_index] # variable voor het data van het categorie
        print("start basic selection sort")
        for index in range(0, len(sorted_steam) - 1):
            min_index = index
            for index_two in range(index+1, len(sorted_steam) - 1):
                if sorted_steam[min_index][sort_on] > sorted_steam[index_two][sort_on]: # kijkt of de minimale grens waar het gesorteerd moet worden op de gesorteerd lijst of het groter is dan de gesorteerd lijst van het index_Two zo ja defineren dat min index gelijkwaardig staat aan index_two
                    min_index = index_two
            sorted_steam[index], sorted_steam[min_index] = sorted_steam[min_index], sorted_steam[index]
        return sorted_steam


    def QuickSort_process(self, arr, sort_on): # quicksort process

        elements = len(arr)

        # Base case
        if elements < 2:
            return arr

        current_position = 0  # Positie van het scheidingselement

        for i in range(1, elements):  # Partitioning loop
            if arr[i][sort_on] <= arr[0][sort_on]:
                current_position += 1
                temp = arr[i]
                arr[i] = arr[current_position]
                arr[current_position] = temp

        temp = arr[0]
        arr[0] = arr[current_position]
        arr[current_position] = temp # Brengt het pivot naar de juiste positie

        left = sort_func.QuickSort_process(arr[0:current_position], sort_on)  # Sorteert de elementen links van het pivot
        right = sort_func.QuickSort_process(arr[current_position + 1:elements],
                                            sort_on)  # sorteert de elementen rechts van het pivot

        arr = left + [arr[current_position]] + right  # hier word alles samegevoerd

        # print(arr)
        return arr


class Statistiek:
    def __init__(self, list_2):
        self.steam_cath = list_2

    def get_relevante_data(self, given_list, index_location):
        # Zorgt dat alle relevante data bij elkaar wordt gehaald.
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
        # print(int(gemidelde), "gemiddelt aantal", relevant_list[0])
        return gemidelde

    def rnge(self, relevant_list):
        high = max(relevant_list[1:])
        low = min(relevant_list[1:])
        range_uitkomst = high - low
        # print(int(range_uitkomst), "range van", relevant_list[0])
        return range_uitkomst

    def median(self, relevant_list):
        lenght_list = (len(relevant_list) - 1)  # -1 vanwege de tag
        midden_punt = lenght_list // 2
        if lenght_list % 2 == 0:
            mediaan = ((relevant_list[midden_punt] + relevant_list[midden_punt - 1]) / 2)
        else:
            mediaan = relevant_list[midden_punt + 1]  # Tag
        # print(mediaan, "median")
        return mediaan

    def variantie(self, relevant_list):
        var_gemidelde = self.gemiddelde(relevant_list)
        resultaat = 0
        for index in range(1, len(relevant_list)):
            afwijking = relevant_list[index] - var_gemidelde
            resultaat += afwijking * afwijking
        var = resultaat / len(relevant_list)
        # print(int(var), "variantie van", relevant_list[0])
        return var

    def standaard_def(self, relevant_list):
        var_list = self.variantie(relevant_list)
        antwoord = var_list ** (1 / 2)
        # print(int(antwoord), "standaarddeviatie van", relevant_list[0])
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
        # print('Kwartiel 0 t/m 4 en iqr', kwartiel_null, kwartiel_een, kwartiel_twee, kwartiel_drie, kwartiel_vier, iqr)
        return kwartiel_null, kwartiel_een, kwartiel_twee, kwartiel_drie, kwartiel_vier, iqr


class search_binaire:
    def __init__(self):
        self.steam_cath = []

    def binary_search(self, list_al, target, cath):
        midden_punt = (len(list_al) - 1) // 2
        # Binary search met Int om de verschilende games rond het gegeven getal te geven.
        if len(list_al) == 0:
            return []
        if int(list_al[midden_punt][cath]) == target:
            return search_b.get_all(list_al, target, cath)
        if int(list_al[midden_punt][cath]) < target:
            return search_b.binary_search(list_al[midden_punt + 1:], target, cath)
        if int(list_al[midden_punt][cath]) > target:
            return search_b.binary_search(list_al[:midden_punt], target, cath)

    def get_all(self, list_al, target, cath):
        low_num = 0
        high_num = len(list_al) - 1
        while int(list_al[low_num][cath]) < target:
            low_num += 1
        while int(list_al[high_num][cath]) > target:
            high_num -= 1
        return list_al[low_num:high_num + 1]


class node:
    def __init__(self, value=None):
        self.value = value # houd de value van de node in de tree
        self.left_child = None # houd de left child van de node in de tree
        self.right_child = None # houd de right child van de node in de tree
        self.parent = None # houd de parent van de node in de tree


class binary_search_tree:
    def __init__(self):
        self.root = None
        self.node_value = []

    def insert(self, value): # main functie voor het invoegen van een node in de tree
        if self.root == None:
            self.root = node(value) # hier word de node gerest naar een nieuwe node met de vorige waarde
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node): # private functie voor het invoegen van een node in de tree
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)



    def print_tree(self): # main functie voor het printen van het tree
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node): # private functie voor het printen van het tree
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self): # main functie voor het zoeken van het hoogte van de boom
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self, cur_node, cur_height): # private functie voor het zoeken van het hoogte van de boom
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value): # main functie voor het zoeken van een node
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node): # private funcite voor het zoeken van een node
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value): # functie voor het verwijderen van de waarde in de tree
        return self.delete_node(self.find(value))

    def delete_node(self,node): # functie voor het verwijderen van een node in de tree

        if node == None or self.find(node.value) == None:
            print("De node die deleted moet worden is niet gevonden!")
            return None
        def min_value_node(n):
            current=n
            while current.left_child != None:
                current=current.left_child
            return current

        def num_children(n):
            num_children=0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:
            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root=None

        if node_children == 1:
            if node.left_child!=None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent != None:
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child
            child.parent=node_parent


        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value
            self.delete_node(successor)

    def search(self, value): # main functie voor het zoeken van het node in de tree
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node): # private functie voor het zoeken van het node in de tree
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False

    def return_tree(self):
        self.node_value = []
        if self.root != None:
            self._return_tree(self.root)

    def _return_tree(self, cur_node):
        if cur_node != None:
            self._return_tree(cur_node.left_child)
            self.node_value.append(str(cur_node.value))
            self._return_tree(cur_node.right_child)

    def delete_root(self):
        if self.root != None:
            self._delete_root(self.root)

    def _delete_root(self, root):
        self.root = None
        root.left = None
        root.right = None


Startup = StartupApiTi()
Startup.inladen()
Startup.split_list()
sort_func = SortingAlgorithms(Startup.steam_cath)
calc_statistiek = Statistiek(Startup.steam_cath)
search_b = search_binaire()
# search_b.binary_search(sort_func.basic_sort('price'), 5, 17)

# sort_func.QuickSort_process(17)
# Startup.next_part()
# sort_func.QuickSort_process(17)


def fill_tree(tree): # functie voor het vullen van de tree # moet later de waardes van de lijst binnen dit functie zetten.
    list = calc_statistiek.get_relevante_data(Startup.part_list[Startup.part_index], 0)
    list = list[1:]
    for i in list:
        # print(i)
        tree.insert(i)
    return tree

tree = binary_search_tree() # initialiseert de tree
# tree = fill_tree(tree) # vult automatisch de tree
#tree.insert(9) # kunnen handmatig de tree vullen met values
# tree.print_tree() # print de hele tree met de hoogte van de tree
# Startup.next_part()
# fill_tree(tree)



# Startup.next_part()
# fill_tree(tree)
#print(tree.search(10)) # kunnen op een bepaalde value kijken of de value in de tree bestaat zoja geeft het een true statement terug zo niet dan een false statement

# print("boom hoogte: " + str(tree.height()))

# Testing uikomst
# calc_statistiek.gemiddelde(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.rnge(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.median(calc_statistiek.get_relevante_data(sort_func.basic_sort('price'), 17))
# calc_statistiek.variantie(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.standaard_def(calc_statistiek.get_relevante_data(calc_statistiek.steam2, 17))
# calc_statistiek.kwartiel_gen(calc_statistiek.get_relevante_data(sort_func.basic_sort('price'), 17))


