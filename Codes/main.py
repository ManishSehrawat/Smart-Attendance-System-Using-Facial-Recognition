from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep
import webbrowser
import os

from login import Login

class MainClass:
    def __init__(self):
        self.master=Tk()
        self.master.title('loading....')
        self.master.iconbitmap('logo.ico')
        #self.master.state('zoomed')
        self.master.attributes("-fullscreen", True)

        self.bg=PhotoImage(file="ncu2.png")
        self.bg_label = Label(self.master, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.head1_lbl = Label(self.bg_label, text = "STUDENT \nATTENDANCE \nMANAGEMENT \nSYSTEM", fg="#a8403d", 
                        font=("Lucida Grande", 50)).place(relx=0.5, rely=0.45, anchor='center')

        self.logo=PhotoImage(file='logo.png')
        self.logo_label=Label(self.master,image=self.logo, bg='white')
        self.logo_label.place(relx = 0.15, rely = 0.05, anchor ='ne')

        def quitfunc():
            self.master.destroy()
            exit(0)

        for i in range(22):
            Label(self.master, bg="white", width=2, height=1).place(x=(i+24)*22, y=550)
        

        self.master.update()
        self.play_animation()

        self.master.mainloop()
    
    def play_animation(self):
        for i in range(4):
            for j in range(22):
                Label(self.master, bg="#f89421", width=2, height=1).place(x=(j+24)*22, y = 550)
                sleep(0.06)
                self.master.update_idletasks()
                Label(self.master, bg="white", width=2, height=1).place(x=(j+24)*22, y=550)
        self.master.destroy()
        self.open_login_page()

    def open_login_page(self):
        obj=Login()

if __name__=="__main__":
    obj=MainClass()