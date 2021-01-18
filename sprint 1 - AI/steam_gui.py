from tkinter import *
from main import *
from PIL import Image, ImageTk
import tkinter.font as font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Dit is de 4e prototype (Work in process).
# Feedback of ideen zijn altijd welkome!

image_list = {1: 'background_steam.png', 2: 'background.png', 3: 'consulting_logo.png'}
image_resized_list = {}


class SteamGui:
    def __init__(self, parent):
        self.parent = parent
        self.font_type = font.Font(family='Verdana', size=12)
        self.parent.iconbitmap('./img/steam-logo.ico')
        self.parent.title("Steam gedrag inzicht")
        self.parent.geometry("%dx%d+0+0" % (width, height))
        self.frame_holder = Frame(root, bg='#483D8B', borderwidth=5, relief=RIDGE)
        self.frame_holder.pack(fill=BOTH, expand=YES)
        self.frame_holder.grid_rowconfigure(0, weight=1)
        self.frame_holder.grid_columnconfigure(0, weight=1)
        self.catagorie_list = []
        for categorie in Startup.steam_cath[0]:
            self.catagorie_list.append(categorie)
        self.all_frames = {}
        for frame in (FrameOne, FrameTwo, FrameThree, FrameFour, FrameFive, FramesixTree, FramesevenTI):
            this_frame = frame(self.frame_holder, self)
            self.all_frames[frame] = this_frame
            this_frame.grid(row=0, column=0, sticky="nsew")
        self.next_frame(FrameOne)

    def next_frame(self, next_frame):
        frame = self.all_frames[next_frame]
        frame.lift()

    def exit(self):
        self.parent.destroy()

    def create_background_logos(self, frame):
        label = Label(frame, image=image_resized_list[1], bg="#483D8B")
        label.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
        frame.label = Label(frame, image=image_resized_list[3], borderwidth=5, relief=RIDGE)
        frame.label.pack(pady=10, padx=10, anchor=NW)


class FrameOne(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        label = Label(self, text="Main Menu", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        label.pack(pady=80, padx=10)
        f1_button1 = Button(self, text="Exit", bg="#99A3A4", command=lambda: master.exit(), borderwidth=5, relief=RIDGE,
                            font=master.font_type, activebackground='#99A3A4')
        f1_button1.bind("<Return>", lambda event: master.exit())
        f1_button1.pack(pady=10, padx=10, side=BOTTOM)
        f1_button2 = Button(self, text="Toon game name", bg="#99A3A4", command=lambda: master.next_frame(FrameTwo), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button2.bind("<Return>", lambda event: master.next_frame(FrameTwo))
        f1_button2.pack(pady=5, padx=5)
        f1_button3 = Button(self, text="Sorteer games", bg="#99A3A4", command=lambda: master.next_frame(FrameThree), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button3.bind("<Return>", lambda event: master.next_frame(FrameThree))
        f1_button3.pack(pady=5, padx=5)
        f1_button4 = Button(self, text="Game statistieken", bg="#99A3A4", command=lambda: master.next_frame(FrameFour),
                            borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button4.bind("<Return>", lambda event: master.next_frame(FrameFour))
        f1_button4.pack(pady=5, padx=5)
        f1_button5 = Button(self, text="Game prijsen", bg="#99A3A4", command=lambda: master.next_frame(FrameFive),
                            borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button5.bind("<Return>", lambda event: master.next_frame(FrameFive))
        f1_button5.pack(pady=5, padx=5)
        f1_button6 = Button(self, text="Search Tree", bg="#99A3A4", command=lambda: master.next_frame(FramesixTree),
                            borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button6.bind("<Return>", lambda event: master.next_frame(FrameFive))
        f1_button6.pack(pady=5, padx=5)
        f1_button7 = Button(self, text="TI in project", bg="#99A3A4", command=lambda: master.next_frame(FramesevenTI),
                            borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button7.bind("<Return>", lambda event: master.next_frame(FrameFive))
        f1_button7.pack(pady=5, padx=5)


class FrameTwo(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        label = Label(self, text="Game name", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        label.pack(pady=80, padx=10)
        self.label1 = Label(self, text="      ", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        self.label1.pack(pady=10, padx=10)
        self.f2_button2 = Button(self, text="Show game", bg="#99A3A4", command=lambda: self.gui_get_name(),
                            borderwidth=5, relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        self.f2_button2.bind("<Return>", lambda event: self.gui_get_name())
        self.f2_button2.pack(pady=10, padx=10)
        f2_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), self.gui_clean_name()], borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f2_button1.bind("<Return>", lambda event: [master.next_frame(FrameOne), self.gui_clean_name()])
        f2_button1.pack(pady=10, padx=10, side=BOTTOM)


    def gui_get_name(self):
        first_game = Startup.give_name()
        self.label1["text"] = first_game
        self.f2_button2.config(text="Next game")


    def gui_clean_name(self):
        self.label1["text"] = "      "
        self.f2_button2.config(text="Show game")
        Startup.reset_part()


class FrameThree(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        self.sorted_list = []
        label = Label(self, text="Sorting games", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        label.pack(pady=20, padx=10, side=TOP)
        self.sorting_method = ["Insertion Sort", "Selection Sort", "Quiq Sort"]
        self.f3_Spinbox2 = Spinbox(self, values=self.sorting_method, font=master.font_type)
        self.f3_Spinbox2.pack(pady=4, padx=4, side=TOP)
        self.f3_Spinbox = Spinbox(self, values=master.catagorie_list, font=master.font_type)
        self.f3_Spinbox.pack(pady=4, padx=4, side=TOP)
        f3_button2 = Button(self, text="Sort", bg="#99A3A4", borderwidth=5, command=lambda: self.get_sort_method(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button2.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button2.pack(pady=4, padx=4, side=TOP)
        self.f3_textbox = Text(self)
        self.f3_textbox.pack(pady=4, padx=4, side=TOP, fill=Y, expand=YES)
        f3_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), Startup.reset_part(),
                                                                              self.gui_insert_text(" ")], borderwidth=5, relief=RIDGE,
                            font=master.font_type, activebackground='#99A3A4')
        f3_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button1.pack(pady=5, padx=5, side=BOTTOM)
        f3_button3 = Button(self, text="Next list", bg="#99A3A4", command=lambda: self.check_nextlist(), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button3.bind("<Return>", lambda event: self.check_nextlist())
        f3_button3.pack(pady=5, padx=5)


    def get_sort_method(self):
        find = self.f3_Spinbox2.get()
        index = self.sorting_method.index(find)
        search = self.f3_Spinbox.get()
        if index == 0:
            self.sorted_list = sort_func.basic_insertion(search)
        elif index == 1:
            self.sorted_list = sort_func.basic_selection(search)
        elif index == 2:
            sort_on_data = Startup.steam_cath[0].index(search)
            data = Startup.part_list[Startup.part_index]
            self.sorted_list = sort_func.QuickSort_process(data, sort_on_data)
        self.gui_sort(search)


    def gui_sort(self, search):
        # search = self.f3_Spinbox.get()
        # self.sorted_list = sort_func.basic_insertion(search)
        insert_text = "Sorting on " + str(search) + '\n'
        cath_num = Startup.steam_cath[0].index(search)
        for index in range(0, len(self.sorted_list)):
            num = index + 1
            game_name = self.sorted_list[index][1]
            cath = self.sorted_list[index][cath_num]
            if cath_num == 1:
                insert_text += str(num) + " " + str(search) + ": " + str(cath) + '\n'
            else:
                insert_text += str(num) + ' Game: ' + str(game_name) + " " + str(search) + " " + str(cath) + '\n'

        self.gui_insert_text(insert_text)


    def check_nextlist(self):
        Startup.next_part()
        self.get_sort_method()


    def gui_insert_text(self, item):
        self.f3_textbox.config(state=NORMAL)
        self.f3_textbox.delete('1.0', END)
        self.f3_textbox.insert(END, item)
        self.f3_textbox.config(state=DISABLED)



class FrameFour(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        self.statistiek_cath = ['price', 'positive_ratings', 'negative_ratings', 'average_playtime']
        f4_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), self.gui_clean_name()], borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f4_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f4_button1.pack(pady=5, padx=5, side=BOTTOM)
        f4_label = Label(self, text="Statistieken", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        f4_label.pack(pady=10, padx=10, side=TOP)
        self.f4_Spinbox = Spinbox(self, values=self.statistiek_cath, font=master.font_type)
        self.f4_Spinbox.pack(pady=4, padx=4, side=TOP)
        self.f4_button1 = Button(self, text="Calculate Statistics", bg="#99A3A4", borderwidth=5, command=lambda: self.gui_calculate_all(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        self.f4_button1.bind("<Return>", lambda event: self.gui_calculate_all())
        self.f4_button1.pack(pady=4, padx=4, side=TOP)
        self.label1 = Label(self, text="      ", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        self.label1.pack(pady=10, padx=10)
        self.label2 = Label(self, text="      ", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        self.label2.pack(pady=10, padx=10)
        f3_button3 = Button(self, text="Next", bg="#99A3A4", command=lambda: self.check_nextlist(), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button3.bind("<Return>", lambda event: self.check_nextlist())
        f3_button3.pack(pady=5, padx=5, side=BOTTOM)

        self.f3_figure = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.f3_figure, self)
        self.canvas.get_tk_widget().pack(side=TOP, expand=True)
        self.plot = self.f3_figure.gca()


    def gui_calculate_all(self):
        calc = self.f4_Spinbox.get()
        index = Startup.steam_cath[0].index(calc)
        gemid_answer = calc_statistiek.gemiddelde(calc_statistiek.get_relevante_data(Startup.part_list[Startup.part_index], index))
        range_answer = calc_statistiek.rnge(calc_statistiek.get_relevante_data(Startup.part_list[Startup.part_index], index))
        median_answer = calc_statistiek.median(calc_statistiek.get_relevante_data(sort_func.basic_insertion(calc), index))
        var_answer = calc_statistiek.variantie(calc_statistiek.get_relevante_data(Startup.part_list[Startup.part_index], index))
        std_def = calc_statistiek.standaard_def(calc_statistiek.get_relevante_data(Startup.part_list[Startup.part_index], index))
        q0, q1, q2, q3, q4, iqr = calc_statistiek.kwartiel_gen(calc_statistiek.get_relevante_data(sort_func.basic_insertion(calc), index))
        string_one = "Gemiddelde: " + str(round(gemid_answer, 2)) + "  Range: " + str(round(range_answer, 2)) + \
                     " Median: " + str(median_answer) + " Variantie: " + str(round(var_answer, 2))
        string_Two = "Standaarddeviatie: " + str(round(std_def, 2)) + " Kwartiel 0 T/m 4: " + \
                     str(q0) + " " + str(q1) + " " + str(q2) + " " + str(q3) + " " + str(q4) + " IQR: " + str(iqr)
        string_zero = "List: " + str(Startup.part_index + 1)
        self.label1["text"] = string_one
        self.label2["text"] = string_Two
        list_show = calc_statistiek.get_relevante_data(sort_func.basic_insertion(calc), index)
        prep_list = list_show[1:]
        self.plot.clear()
        self.plot.hist(prep_list, bins=10)
        self.plot.set_title(string_zero)
        self.canvas.draw()

    def check_nextlist(self):
        Startup.next_part()
        self.gui_calculate_all()

    def gui_clean_name(self):
        self.label1["text"] = "      "
        self.label2["text"] = "      "
        Startup.reset_part()


class FrameFive(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        f5_label = Label(self, text="Game prijsen lijst", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        f5_label.pack(pady=10, padx=10, side=TOP)
        f5_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), Startup.reset_part()], borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f5_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f5_button1.pack(pady=5, padx=5, side=BOTTOM)
        self.f5_entry = Entry(self)
        self.f5_entry.pack(pady=5, padx=5)
        self.f4_button1 = Button(self, text="Ok", bg="#99A3A4", borderwidth=5, command=lambda: self.check_input(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        self.f4_button1.bind("<Return>", lambda event: self.check_input())
        self.f4_button1.pack(pady=4, padx=4, side=TOP)
        self.f4_textbox = Text(self)
        self.f4_textbox.pack(pady=4, padx=4, side=TOP, fill=Y, expand=YES)
        f5_button1 = Button(self, text="Next list", bg="#99A3A4", command=lambda: self.check_nextlist(), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f5_button1.bind("<Return>", lambda event: self.check_nextlist())
        f5_button1.pack(pady=5, padx=5)

    def check_input(self):
        check = self.f5_entry.get()
        if check.isdigit():
            self.get_gui_list(float(check))

    def get_gui_list(self, target):
        list = sort_func.basic_insertion('price')
        search_list = search_b.binary_search(list, target, 17)
        insert_text = "Searching on " + str(target) + '\n'
        for index in range(0, (len(search_list)-1)):
            num = index + 1
            game_name = search_list[index][1]
            price = search_list[index][17]
            insert_text += str(num) + ' Game: ' + str(game_name) + ' Price: ' + str(price) + '\n'
        self.gui_insert_text(insert_text)

    def check_nextlist(self):
        Startup.next_part()
        self.check_input()

    def gui_insert_text(self, item):
        self.f4_textbox.config(state=NORMAL)
        self.f4_textbox.delete('1.0', END)
        self.f4_textbox.insert(END, item)
        self.f4_textbox.config(state=DISABLED)



class FramesixTree(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        f6_label = Label(self, text="Search Tree", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        f6_label.pack(pady=20, padx=10, side=TOP)
        f6_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), Startup.reset_part()], borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f6_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f6_button1.pack(pady=10, padx=10, side=BOTTOM)
        f6_button2 = Button(self, text="Load tree", bg="#99A3A4", borderwidth=5, command=lambda: self.load_tree(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f6_button2.bind("<Return>", lambda event: self.load_tree())
        f6_button2.pack(pady=4, padx=4)
        self.f6_textbox = Text(self)
        self.f6_textbox.pack(pady=4, padx=4, side=TOP, fill=Y, expand=YES)
        f6_button3 = Button(self, text="Next tree", bg="#99A3A4", borderwidth=5, command=lambda: self.load_next_tree(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f6_button3.bind("<Return>", lambda event: self.load_next_tree())
        f6_button3.pack(pady=4, padx=4)

    def load_tree(self):
        fill_tree(tree)
        print(tree.return_tree())
        return

    def load_next_tree(self):
        Startup.next_part()
        fill_tree(tree)
        tree.print_tree()

    def gui_insert_text(self, item):
        self.f6_textbox.config(state=NORMAL)
        self.f6_textbox.delete('1.0', END)
        self.f6_textbox.insert(END, item)
        self.f6_textbox.config(state=DISABLED)


class FramesevenTI(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        f7_label = Label(self, text="TI in project", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        f7_label.pack(pady=80, padx=10, side=TOP)
        f7_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: [master.next_frame(FrameOne), Startup.reset_part()], borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f7_button1.pack(pady=10, padx=10, side=BOTTOM)
        f7_button2 = Button(self, text="Show1", bg="#99A3A4", borderwidth=5, command=lambda: self.show1(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button2.bind("<Return>", lambda event: self.show1())
        f7_button2.pack(pady=4, padx=4)
        f7_button3 = Button(self, text="Show2", bg="#99A3A4", borderwidth=5, command=lambda: self.show2(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button3.bind("<Return>", lambda event: self.show2())
        f7_button3.pack(pady=4, padx=4)
        f7_button4 = Button(self, text="Show3", bg="#99A3A4", borderwidth=5, command=lambda: self.show3(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button4.bind("<Return>", lambda event: self.show3())
        f7_button4.pack(pady=4, padx=4)
        f7_button5 = Button(self, text="Show4", bg="#99A3A4", borderwidth=5, command=lambda: self.show4(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button5.bind("<Return>", lambda event: self.show4())
        f7_button5.pack(pady=4, padx=4)
        f7_button6 = Button(self, text="Show5", bg="#99A3A4", borderwidth=5, command=lambda: self.show5(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f7_button6.bind("<Return>", lambda event: self.show5())
        f7_button6.pack(pady=4, padx=4)


    def show1(self):
        return

    def show2(self):
        return

    def show3(self):
        return

    def show4(self):
        return

    def show5(self):
        return



def resize_image(item, n_width, n_height, num):
    open_image = Image.open(("./img/" + item))
    resized_image = open_image.resize((n_width, n_height), Image.ANTIALIAS)
    complete_image = ImageTk.PhotoImage(resized_image)
    image_resized_list.update({num: complete_image})


def resize_image_size(width, height):
    resize_image(image_list[1], width, height, 1)
    resize_image(image_list[2], width, height, 2)
    resize_image(image_list[3], int(width * 0.104166667), int(height * 0.06944444), 3)


root = Tk()
width = int(root.winfo_screenwidth() / 1.8)
height = int(root.winfo_screenheight() / 1.1)
resize_image_size(width, height)
steam_gui = SteamGui(root)
root.mainloop()
