from tkinter import *

# Dit is de 1e prototype ((Work in process/Niet af)).
# Het gaat meer om de bouw in code volgens de manier van Tinking in tkinter(canvas)
#
# Feedback of ideen zijn altijd welkome!


class SteamGui:
    def __init__(self, parent):
        self.parent = parent
        width = int(parent.winfo_screenwidth() / 2)
        height = int(parent.winfo_screenheight() / 1.5)
        self.parent.iconbitmap('./img/steam-logo.ico')
        self.parent.title("Steam gedrag inzicht??")
        self.parent.geometry("%dx%d+0+0" % (width, height))
        self.frame_holder = Frame(root, bg='red', borderwidth=5, relief=RIDGE)
        self.frame_holder.pack(fill=BOTH, expand=YES)
        self.frame_holder.grid_rowconfigure(0, weight=1)
        self.frame_holder.grid_columnconfigure(0, weight=1)
        self.all_frames = {}
        for frame in (FrameOne, FrameTwo):
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
        label = Label(frame, text="background", bg="#483D8B")
        label.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
        frame.label = Label(frame, text="Logo", bg="yellow", borderwidth=5, relief=RIDGE)
        frame.label.pack(pady=10, padx=10, anchor=NW)


class FrameOne(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self,parrent)
        master.create_background_logos(self)
        label = Label(self, text="Begin Scherm", bg="blue", borderwidth=5, relief=RIDGE)
        label.pack(pady=10, padx=10)
        f1_button1 = Button(self, text="Show Naam functie button", command=lambda: self.deze_func_bestaat_niet(), borderwidth=5, relief=RIDGE)
        f1_button1.bind("<Return>", lambda event: self.deze_func_bestaat_niet())
        f1_button1.pack(pady=10, padx=10)
        self.label1 = Label(self, text="NAAM HIER", borderwidth=5, relief=RIDGE)
        self.label1.pack(pady=10, padx=10)
        f1_button3 = Button(self, text="Exit", command=lambda: master.exit(), borderwidth=5, relief=RIDGE)
        f1_button3.bind("<Return>", lambda event: master.exit())
        f1_button3.pack(pady=10, padx=10, side=BOTTOM)
        f1_button2 = Button(self, text="Volgende frame", command=lambda: master.next_frame(FrameTwo), borderwidth=5, relief=RIDGE)
        f1_button2.bind("<Return>", lambda event: master.next_frame(FrameTwo))
        f1_button2.pack(pady=10, padx=10,  side=BOTTOM)


    def deze_func_bestaat_niet(self):
        # De functie voor naam moet nog komen in andere script!
        self.label1["text"] = "TESTING NAAM"


class FrameTwo(Frame):
    def __init__(self, parrent, master):
        Frame.__init__(self, parrent)
        master.create_background_logos(self)
        label = Label(self, text="FrameTwo", bg="blue", borderwidth=5, relief=RIDGE)
        label.pack(pady=10, padx=10)
        f2_button1 = Button(self, text="Back", command=lambda: master.next_frame(FrameOne), borderwidth=5, relief=RIDGE)
        f2_button1.bind("<Return>", lambda event: master.next_frame(FrameOne))
        f2_button1.pack(pady=10, padx=10, side=BOTTOM)




root = Tk()
steam_gui = SteamGui(root)
root.mainloop()
#
# self.background_frame = Frame(root, bg='red', borderwidth=5, relief=RIDGE)
# self.background_frame.pack(fill=BOTH, expand=YES)
