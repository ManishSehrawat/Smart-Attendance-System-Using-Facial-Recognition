from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

from menu import Menu

class Login:
    def __init__(self):
        self.root=Tk()
        self.root.title("Login")
        self.root.iconbitmap('logo.ico')
        self.root.attributes('-fullscreen', True)

        self.var_username=StringVar()
        self.var_password=StringVar()

        bg_img=Image.open("ncu2.png")
        #bg_img=bg_img.resize((1600,710),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(bg_img)
        bg_lbl=Label(self.root,image=self.bg_img)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=610, y=190, width=340, height=430)

        user_img = Image.open("user2.png")
        user_img=user_img.resize((100,100),Image.ANTIALIAS)
        self.user_img = ImageTk.PhotoImage(user_img)
        user_img_lbl = Label(self.root, image=self.user_img, bg="black")
        user_img_lbl.place(x=730, y=200,width=100,height=100)

        head=Label(frame, text="Get Started", font=("times new roman",20,"bold"), fg="white", bg="black")
        head.place(x=95, y=135)

        username_img=Image.open("user2.png")
        username_img=username_img.resize((25,25),Image.ANTIALIAS)
        self.username_img=ImageTk.PhotoImage(username_img)
        username_img_lbl=Label(frame, image=self.username_img, bg="black")
        username_img_lbl.place(x=40, y=175, height=25, width=25)

        username_lbl=Label(frame, text="Username", font=("times new roman", 15,"bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=175)

        password_img = Image.open("lock2.png")
        password_img = password_img.resize((25,25),Image.ANTIALIAS)
        self.password_img=ImageTk.PhotoImage(password_img)
        password_img_lbl=Label(frame, image=self.password_img, bg="black")
        password_img_lbl.place(x=40,y=245, height=25, width=25)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y =245)

        username_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_username)
        username_entry.place(x=40, y=205, width=270)

        password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_password, show="*")
        password_entry.place(x=40, y=275, width=270)

        login_btn = Button(frame, text="login",font=("times new roman", 15, "bold"), bd=3, 
                            relief=RIDGE, fg="#a93e3a", bg="#f8951b", activeforeground="#a93e3a", 
                            activebackground="#f8951b", command=self.login)
        #14cfff
        login_btn.place(x=110, y=320, width=120, height=35)


        forgot_btn = Button(frame, text="Forgot Password", font=("times new roman", 10, "bold", "underline"), 
                    bg="black", fg="white", activebackground="black", activeforeground="white", borderwidth=0, command=self.forgot)
        forgot_btn.place(x=40, y=370)


        def quitApp():
            self.root.destroy()
            exit(0)
        quit_img=Image.open("quit.png")
        quit_img=quit_img.resize((50,50),Image.ANTIALIAS)
        self.quit_img=ImageTk.PhotoImage(quit_img)
        quit_btn=Button(self.root, image=self.quit_img,cursor="hand2",  
                        command=quitApp, bg="black", activebackground="black")
        quit_btn.place(x=1480,y=0)


        #self.root.mainloop()


#---------------------------------login function-------------------------------------------------
    def login(self):
        if self.var_username.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
            my_cursor = conn.cursor()
            my_cursor.execute("Select name from login_info where username=%s and password=%s",(self.var_username.get(), self.var_password.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Invalid!", "Invalid username or password")
                flag=0
            else :
                messagebox.showinfo("Welcome", "Welcome "+str(row[0]))
                self.var_password.set("")
                self.var_username.set("")
                flag=1
            conn.commit()
            conn.close()
            if flag==1:
                self.open_menu()

    def open_menu(self):
        self.new_window = Toplevel(self.root)
        self.menu_obj = Menu(self.new_window)


    def forgot(self):
        if self.var_username.get()=="":
            messagebox.showerror("Error", "Enter username")
        else:
            conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
            my_cursor = conn.cursor()
            my_cursor.execute("Select name from login_info where username=%s",(self.var_username.get(),))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Invalid!", "The entered username does not exist!")
            else :
                messagebox.showinfo("Password reset", "Dear \""+str(row[0])+"\" Please chek your registered e-mail ID to set new password")
            conn.commit()
            conn.close()
if __name__=="__main__":
    root=Tk()
    obj = Login()
    #root.mainloop()