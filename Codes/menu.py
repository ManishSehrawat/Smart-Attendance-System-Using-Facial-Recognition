from helpdesk import Helpdesk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep
import webbrowser
import os

from student import Student
from train import Train
from training import Train
from records import Attendance  
from recognition import Recognition

class Menu:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)

        bg_img=Image.open("ncu.png")
        bg_img=bg_img.resize((1600,710),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(bg_img)
        bg_lbl=Label(self.root,image=self.bg_img)
        bg_lbl.place(x=0,y=130,width=1600,height=800)
        #bg_lbl.pack(pady=10)
        
        def visitSite():
            url="https://www.ncuindia.edu/"
            webbrowser.open(url)

        logo_img=Image.open("logo.png")
        logo_img=logo_img.resize((300,130),Image.ANTIALIAS)
        self.logo_img=ImageTk.PhotoImage(logo_img)
        logo_btn=Button(self.root,image=self.logo_img, bg='white', relief=RAISED, command=visitSite, cursor="hand2")
        logo_btn.place(x=0,y=0,height=130)
        logo_btn.bind("<Enter>", lambda e: logo_btn.config(bg='#DCDCDC'))
        logo_btn.bind("<Leave>", lambda e: logo_btn.config( bg='white'))

        img1=Image.open("img1.png")
        img1=img1.resize((400,130),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)
        img1_lbl=Label(self.root, image=self.img1)
        img1_lbl.place(x=300,y=0,height=130)

        img2=Image.open("img2.jpg")
        img2=img2.resize((335,130),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)
        img2_lbl=Label(self.root, image=self.img2)
        img2_lbl.place(x=700,y=0,height=130)

        img3=Image.open("img3.png")
        img3=img3.resize((315,130),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img3)
        img3_lbl=Label(self.root, image=self.img3)
        img3_lbl.place(x=1035,y=0,height=130)

        def quitApp():
            self.root.destroy()
            exit(0)
        quit_img=Image.open("quit.png")
        quit_img=quit_img.resize((180,100),Image.ANTIALIAS)
        self.quit_img=ImageTk.PhotoImage(quit_img)
        quit_btn=Button(self.root, text = "QUIT",fg="#a8403d", 
                        compound=TOP, relief=RAISED, image=self.quit_img,  
                        bg='white', command=quitApp,font=("arial",10,"bold"),  
                        cursor="hand2")
        quit_btn.place(x=1350,y=0,height=130)
        quit_btn.bind("<Enter>", lambda e: quit_btn.config(bg='#DCDCDC'))
        quit_btn.bind("<Leave>", lambda e: quit_btn.config( bg='white'))


        logout_img= Image.open('logout.png')
        logout_img=logout_img.resize((70,70), Image.ANTIALIAS)
        self.logout_img =ImageTk.PhotoImage(logout_img)
        logout_btn = Button(self.root, text="LOGOUT", image=self.logout_img, 
                    relief=RAISED,  cursor="hand2", compound=LEFT,
                    font=("times new roman", 22),fg="#a8403d",  bg="white", command=self.root.destroy)
        logout_btn.place(x=1300, y=750)


        head_lbl=Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM", 
                        font=("times new roman",35, "bold"), bg='white', fg='#a8403d', padx=50)
        head_lbl.place(x=0,y=0, width=1530, height=45)
        
       
        details_img=Image.open("details.png")
        details_img=details_img.resize((190,210), Image.ANTIALIAS)
        self.details_img = ImageTk.PhotoImage(details_img)
        details_btn = Button(self.root, text="STUDENT \nDETAILS", compound=TOP,
                             relief=RAISED, image=self.details_img,
                            cursor="hand2",font=("times new roman", 18), command=self.open_students)
        details_btn.place(x=120, y=390)

        train_img=Image.open("train.jpg")
        train_img=train_img.resize((190,210), Image.ANTIALIAS)
        self.train_img = ImageTk.PhotoImage(train_img)
        train_btn = Button(self.root, text="TRAIN \nSYSTEM", compound=TOP,
                             relief=RAISED, image=self.train_img,
                            cursor="hand2",font=("times new roman", 18), command=self.open_training)
        train_btn.place(x=340, y=390)

        recog_img=Image.open("recog.jpg")
        recog_img=recog_img.resize((190,210), Image.ANTIALIAS)
        self.recog_img = ImageTk.PhotoImage(recog_img)
        recog_btn = Button(self.root, text="FACE\nRECOGNIZER", compound=TOP,
                             relief=RAISED, image=self.recog_img,
                            cursor="hand2",font=("times new roman", 18), command=self.open_recognition)
        recog_btn.place(x=560, y=390)

        attendance_img=Image.open("attendance.png")
        attendance_img=attendance_img.resize((190,210), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(attendance_img)
        attendance_btn = Button(self.root, text="ATTENDANCE\nREPORT", compound=TOP,
                             relief=RAISED, image=self.attendance_img,
                            cursor="hand2",font=("times new roman", 18), command=self.open_records)
        attendance_btn.place(x=780, y=390)

        photos_img=Image.open("photos.png")
        photos_img=photos_img.resize((190,210), Image.ANTIALIAS)
        self.photos_img = ImageTk.PhotoImage(photos_img)
        photos_btn = Button(self.root, text="VIEW\nPHOTOS", compound=TOP,
                             relief=RAISED, image=self.photos_img,
                            cursor="hand2",font=("times new roman", 18), command=self.open_photos)
        photos_btn.place(x=1000, y=390)

        help_desk_img = Image.open("helpdesk.png")
        help_desk_img=help_desk_img.resize((190,210), Image.ANTIALIAS)
        self.help_desk_img = ImageTk.PhotoImage(help_desk_img)
        help_desk_btn = Button(self.root, text="HELP\nDESK", compound=TOP, 
                        relief=RAISED, image=self.help_desk_img,
                        cursor="hand2",font=("times new roman",18), command=self.open_help_desk)
        help_desk_btn.place(x=1220, y=390)


        #self.root.mainloop()


    def open_students(self):
        self.new_window = Toplevel(self.root)
        self.students_obj = Student(self.new_window)
        #obj=Student(self.root)
        #self.root.mainloop()

    def open_photos(self):
        os.startfile("images")
    
    def open_training(self):
        self.new_window = Toplevel(self.root)
        self.training_obj = Train(self.new_window)

    def open_recognition(self):
        self.new_window = Toplevel(self.root)
        self.recognition_obj = Recognition(self.new_window)

    def open_records(self):
        self.new_window = Toplevel(self.root)
        self.records_obj = Attendance(self.new_window)

    def open_help_desk(self):
        self.new_window = Toplevel(self.root)
        self.helpdesk_obj = Helpdesk(self.new_window)
        
if __name__=="__main__":
    root = Tk()
    obj=Menu(root)
    root.mainloop()