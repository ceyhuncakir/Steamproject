from tkinter import *
from main import *
from PIL import Image, ImageTk
import tkinter.font as font


# Dit is de 3e prototype (Work in process).
# Feedback of ideen zijn altijd welkome!

image_list = {1: 'background_steam.png', 2: 'background.png', 3: 'consulting_logo.png'}
image_resized_list = {}


class SteamGui:
    def __init__(self, parent):
        self.parent = parent
        self.font_type = font.Font(family='Verdana', size=12)
        self.parent.iconbitmap('./img/steam-logo.ico')
        self.parent.title("Steam gedrag inzicht??")
        self.parent.geometry("%dx%d+0+0" % (width, height))
        self.frame_holder = Frame(root, bg='#483D8B', borderwidth=5, relief=RIDGE)
        self.frame_holder.pack(fill=BOTH, expand=YES)
        self.frame_holder.grid_rowconfigure(0, weight=1)
        self.frame_holder.grid_columnconfigure(0, weight=1)
        self.catagorie_list = []
        for categorie in Startup.steam_cath[0]:
            self.catagorie_list.append(categorie)
        self.all_frames = {}
        for frame in (FrameOne, FrameTwo, FrameThree, FrameFour):
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
        f1_button3 = Button(self, text="Exit", bg="#99A3A4", command=lambda: master.exit(), borderwidth=5, relief=RIDGE,
                            font=master.font_type, activebackground='#99A3A4')
        f1_button3.bind("<Return>", lambda event: master.exit())
        f1_button3.pack(pady=10, padx=10, side=BOTTOM)
        f1_button2 = Button(self, text="Show game names", bg="#99A3A4", command=lambda: master.next_frame(FrameTwo), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button2.bind("<Return>", lambda event: master.next_frame(FrameTwo))
        f1_button2.pack(pady=5, padx=5)
        f1_button3 = Button(self, text="Sorteer games", bg="#99A3A4", command=lambda: master.next_frame(FrameThree), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button3.bind("<Return>", lambda event: master.next_frame(FrameThree))
        f1_button3.pack(pady=5, padx=5)
        f1_button4 = Button(self, text="Game Statistieken", bg="#99A3A4", command=lambda: master.next_frame(FrameFour),
                            borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f1_button4.bind("<Return>", lambda event: master.next_frame(FrameFour))
        f1_button4.pack(pady=5, padx=5)


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


class FrameThree(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        self.sorted_list = []
        label = Label(self, text="Sorting games", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        label.pack(pady=20, padx=10, side=TOP)
        self.f3_Spinbox = Spinbox(self, values=master.catagorie_list, font=master.font_type)
        self.f3_Spinbox.pack(pady=4, padx=4, side=TOP)
        f3_button2 = Button(self, text="Sort", bg="#99A3A4", borderwidth=5, command=lambda: self.gui_sort(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button2.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button2.pack(pady=4, padx=4, side=TOP)
        self.f3_textbox = Text(self)
        self.f3_textbox.pack(pady=4, padx=4, side=TOP, fill=Y, expand=YES)
        f3_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: master.next_frame(FrameOne), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button1.pack(pady=5, padx=5, side=BOTTOM)


    def gui_sort(self):
        search = self.f3_Spinbox.get()
        self.sorted_list = sort_func.basic_sort(search)
        insert_text = "Sorting on " + str(search) + '\n'
        for index in range(0, len(self.sorted_list)):
            num = index + 1
            game_name = self.sorted_list[index][1]
            date = self.sorted_list[index][2]
            insert_text += str(num) + ' Game: ' + str(game_name) + ' Release date: ' + str(date) + '\n'
        self.gui_insert_text(insert_text)


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
        f4_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: master.next_frame(FrameOne), borderwidth=5,
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

    def gui_calculate_all(self):
        calc = self.f4_Spinbox.get()
        index = Startup.steam_cath[0].index(calc)
        gemid_answer = calc_statistiek.gemiddelde(calc_statistiek.get_relevante_data(calc_statistiek.steam2, index))
        range_answer = calc_statistiek.rnge(calc_statistiek.get_relevante_data(calc_statistiek.steam2, index))
        # median_answer = calc_statistiek.median(calc_statistiek.get_relevante_data(sort_func.basic_sort(calc), index))
        var_answer = calc_statistiek.variantie(calc_statistiek.get_relevante_data(calc_statistiek.steam2, index))
        std_def = calc_statistiek.standaard_def(calc_statistiek.get_relevante_data(calc_statistiek.steam2, index))
        # q0, q1, q2, q3, q4, iqr = calc_statistiek.kwartiel_gen(calc_statistiek.get_relevante_data(sort_func.basic_sort(calc), index))
        string_one = "Gemiddelde: " + str(round(gemid_answer, 2)) + "  Range: " + str(round(range_answer, 2)) + \
                     " Median: Off " + " Variantie: " + str(round(var_answer, 2))
        string_Two = "Standaarddeviatie: " + str(round(std_def, 2)) + " Kwartiel 0 T/m 4: OFF "
        self.label1["text"] = string_one
        self.label2["text"] = string_Two


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
