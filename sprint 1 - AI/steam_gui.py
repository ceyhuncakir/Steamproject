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
        for categorie in steam[0]:
            self.catagorie_list.append(categorie)
        self.all_frames = {}
        for frame in (FrameOne, FrameTwo, FrameThree):
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
        first_game = give_name()
        self.label1["text"] = first_game
        self.f2_button2.config(text="Next game")


    def gui_clean_name(self):
        self.label1["text"] = "      "
        self.f2_button2.config(text="Show game")


class FrameThree(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        self.sorted_list = {}
        label = Label(self, text="Sorting games", bg="#99A3A4", borderwidth=5, relief=RIDGE, font=master.font_type)
        label.pack(pady=20, padx=10, side=TOP)
        self.f3_Spinbox = Spinbox(self, values=master.catagorie_list, font=master.font_type)
        self.f3_Spinbox.pack(pady=4, padx=4, side=TOP)
        f3_button2 = Button(self, text="Sort", bg="#99A3A4", borderwidth=5, command=lambda: self.gui_sort(),
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button2.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button2.pack(pady=4, padx=4, side=TOP)
        # f3_button3 = Button(self, text="Next", bg="#99A3A4", borderwidth=5,
        #                     relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        # f3_button3.bind("<Return>", lambda event: master.next_frame(FrameOne))
        # f3_button3.pack(pady=4, padx=4, side=TOP)
        self.f3_textbox = Text(self)
        self.f3_textbox.pack(pady=4, padx=4, side=TOP, fill=Y, expand=YES)
        f3_button1 = Button(self, text="Back", bg="#99A3A4", command=lambda: master.next_frame(FrameOne), borderwidth=5,
                            relief=RIDGE, font=master.font_type, activebackground='#99A3A4')
        f3_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f3_button1.pack(pady=4, padx=4, side=BOTTOM)


    def gui_sort(self):
        search = self.f3_Spinbox.get()
        self.sorted_list = sort(search, 1)
        inserting = ''
        num = 0
        for key, item in self.sorted_list.items():
            a = str(num) + ": "
            b = item['name']
            c = item['developer']
            inserting += str(a) + 'Name: ' + str(b) + "  " + str(search) + ": " + str(item[search]) + '\n'
            num += 1
        self.gui_insert_text(inserting)


    def gui_insert_text(self, item):
        self.f3_textbox.config(state=NORMAL)
        self.f3_textbox.delete('1.0', END)
        self.f3_textbox.insert(END, item)
        self.f3_textbox.config(state=DISABLED)


def resize_image(item, n_width, n_height, num):
    open_image = Image.open(("./img/" + item))
    resized_image = open_image.resize((n_width, n_height), Image.ANTIALIAS)
    complete_image = ImageTk.PhotoImage(resized_image)
    image_resized_list.update({num: complete_image})


def resize_image_size(width, height):
    resize_image(image_list[1], width, height, 1)
    resize_image(image_list[2], width, height, 2)
    resize_image(image_list[3], int(width * 0.104166667), int(height * 0.06944444), 3)


inladen()
root = Tk()
width = int(root.winfo_screenwidth() / 1.8)
height = int(root.winfo_screenheight() / 1.1)
resize_image_size(width, height)
steam_gui = SteamGui(root)
root.mainloop()
