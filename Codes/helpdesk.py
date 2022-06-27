import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkcalendar import*
from PIL import Image, ImageTk

class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)
        root.configure(bg="#5eb6b8")
        
        head_lbl=Label(self.root, text="HELP DESK", 
                        font=("times new roman",60, "bold"), bg='#5E8EB8', fg='white', padx=50)
        head_lbl.place(x=0,y=0, width=1540, height=100)

        side_img = Image.open("helpdesk_side.jpg")
        side_img= side_img.resize((700,700), Image.ANTIALIAS)
        self.side_img = ImageTk.PhotoImage(side_img)
        side_img_lbl = Label(self.root, image=self.side_img)
        side_img_lbl.place(x=100, y=120)

        top_img = Image.open("helpdesk_img.png")
        top_img= top_img.resize((90,90), Image.ANTIALIAS)
        self.top_img = ImageTk.PhotoImage(top_img)
        top_img_lbl = Label(self.root, image=self.top_img, bg="#5E8EB8")
        top_img_lbl.place(x=400, y=0)

        def quitApp():
            self.root.destroy()
            exit(0)
        quit_img=Image.open("quitapp.png")
        quit_img=quit_img.resize((90,90),Image.ANTIALIAS)
        self.quit_img=ImageTk.PhotoImage(quit_img)
        quit_btn=Button(self.root, image=self.quit_img,cursor="hand2",  
                        command=quitApp, bg="#5E8EB8", activebackground="#5E8EB8")
        quit_btn.place(x=1430,y=0)

        back_img = Image.open("previous.png")
        back_img=back_img.resize((90,90),Image.ANTIALIAS)
        self.back_img = ImageTk.PhotoImage(back_img)
        back_btn = Button(self.root, image=self.back_img, 
                          bg="#5E8EB8", activebackground = "#5E8EB8",fg="white", cursor="hand2", command=self.root.destroy)
        back_btn.place(x=10, y=0)

        head_lbl = Label(self.root,text="We are here to help you!",font=("times new roman", 40), fg="white", bg="#5eb6b8")
        head_lbl.place(x=915, y=170)

        mail_img = Image.open("email.png")
        mail_img=mail_img.resize((60,60), Image.ANTIALIAS)
        self.mail_img = ImageTk.PhotoImage(mail_img)
        mail_img_lbl = Label(self.root, image=self.mail_img, bg="#5eb6b8")
        mail_img_lbl.place(x=915,y=270)
        mail_lbl = Label(self.root, text="helpdesk@ncuindia.edu", font=("times new roman", 30), fg="#373e9f", bg="#5eb6b8")
        mail_lbl.place(x=1000,y=280)

        phone_img = Image.open("call.png")
        phone_img=phone_img.resize((60,60), Image.ANTIALIAS)
        self.phone_img = ImageTk.PhotoImage(phone_img)
        phone_img_lbl = Label(self.root, image=self.phone_img, bg="#5eb6b8")
        phone_img_lbl.place(x=915,y=370)
        phone_lbl = Label(self.root, text=" 0124 236 5811", font=("times new roman", 30), fg="#373e9f", bg="#5eb6b8")
        phone_lbl.place(x=1000, y=380)

        location_img = Image.open("pin.png")
        location_img=location_img.resize((60,60), Image.ANTIALIAS)
        self.location_img = ImageTk.PhotoImage(location_img)
        location_img_lbl = Label(self.root, image=self.location_img, bg="#5eb6b8")
        location_img_lbl.place(x=915,y=470)
        location_lbl = Label(self.root, text="Near Rotary Public School \n Cartarpuri Alias,Huda, \nSector 23A, Gurugram,\n Haryana 122017",
        font=("times new roman", 30), fg="#373e9f", bg="#5eb6b8" )
        location_lbl.place(x=1000, y=480)


if __name__=="__main__":
    root=Tk()
    obj = Helpdesk(root)
    root.mainloop()
