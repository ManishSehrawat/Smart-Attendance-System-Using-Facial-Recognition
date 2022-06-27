import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkcalendar import*
from PIL import Image, ImageTk
from datetime import date
from tkinter import messagebox
import os
import mysql.connector
import cv2
import webbrowser
import numpy as np

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)

        #-------Variables-----------
        self.var_school = StringVar()
        self.var_prog = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_gender =StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_father =StringVar()
        self.var_address = StringVar()
        self.var_search = StringVar()
        self.var_searchby = StringVar()

        bg_img=Image.open("ncu.png")
        bg_img=bg_img.resize((1600,710),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(bg_img)
        bg_lbl=Label(self.root,image=self.bg_img)
        bg_lbl.place(x=0,y=130,width=1600,height=800)
        #bg_lbl.pack(pady=5)
        
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
                        bg='white', command=quitApp,font=(9),  
                        cursor="hand2")
        quit_btn.place(x=1350,y=0,height=130)
        quit_btn.bind("<Enter>", lambda e: quit_btn.config(bg='#DCDCDC'))
        quit_btn.bind("<Leave>", lambda e: quit_btn.config( bg='white'))


        head_lbl=Label(bg_lbl, text="STUDENT DETAILS MANAGEMENT SYSTEM", 
                        font=("times new roman",35, "bold"), bg='white', fg='#a8403d', padx=50)
        head_lbl.place(x=0,y=0, width=1530, height=45)
    

        frame = Frame(bg_lbl, bd=2, bg="white")
        frame.place(x=15, y=55, width=1500, height=660)

        #left level frame
        left_frame = LabelFrame(frame, bd=2, relief=RIDGE, bg="white", text = "Student Details", font=("times new roman", 18,"bold"))
        left_frame.place(x=20, y=10, width = 715, height = 620)
        
        student_img = Image.open("student.jpg")
        student_img = student_img.resize((700,150), Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(student_img)
        left_frame_img = Label(left_frame, image=self.student_img)
        left_frame_img.place(x=5, y=0, width=702, height=150)

        # COURSE DETAILS
        course_frame = LabelFrame(left_frame, text = "Course Details", font=("times new roman", 12, "bold"), bd=2, bg="white", relief=RIDGE)
        course_frame.place(x=5, y=135, width=702, height=100)

        dept_label = Label(course_frame, text="School", font=("times new roman", 12, "bold"), bg="white", width=10)
        dept_label.grid(row=0, column=0, padx=10, pady=5)
        self.dept_combo = ttk.Combobox(course_frame, state="readonly", textvariable=self.var_school, font=("times new roman", 10), width=25)
        self.dept_combo['values'] = ("Select", "School of engineering", "School of law", "School of management", "School of applied sciences") 
        self.dept_combo.current(0)
        self.dept_combo.grid(row=0, column=1, padx=10, pady=5)

        def course_options(*args):
            if self.dept_combo.get() == "School of engineering":
                if self.programme_combo.get()=="Undergraduate":
                    self.course_combo['values'] = ("Select","Btech. in CSE", "Btech. in ME", "Btech. in ECE", "Btech. in CE")
                elif self.programme_combo.get()=="Postgraduate":
                    self.course_combo['values'] = ("Select","Mtech. in CSE", "Mtech. in ME", "Btech. in ECE", "Btech. in CE")
                elif self.programme_combo.get() == "Research":
                    self.course_combo["values"] = ("Select","Ph.D in CSE", "Ph.D in ME", "Ph.D in ECE", "Ph.D in CE")
            elif self.dept_combo.get() == "School of law":
                if self.programme_combo.get()=="Undergraduate":
                    self.course_combo['values'] = ("Select","BBA.LL.B.")
                elif self.programme_combo.get() == "Postgraduate":
                    self.course_combo['values'] = ("Select","Master of laws")
                elif self.programme_combo.get() == "Research":
                    self.course_combo['values'] = ("Select", "Ph.D (law)")
            elif self.dept_combo.get() == "School of management":
                if self.programme_combo.get() == "Undergraduate":
                    self.course_combo['values'] = ("Select", "BA (Hons) Psychology", "BA Economics (Hons)", "BBA", "B.Com.")
                elif self.programme_combo.get() == "Postgraduate":
                    self.course_combo["values"] = ("Select", "MBA")
                elif self.programme_combo.get() == "Research":
                    self.course_combo['values'] = ("Select", "Ph.D")
            elif self.dept_combo.get() == "School of applied sciences":
                if self.programme_combo.get() == "Undergraduate":
                    self.course_combo['values'] = ("Select", "B.Sc.(Hons.) in Chemistry", "B.Sc.(Hons.) in Physics", "B.Sc. Maths (Hons.)")
                elif self.programme_combo.get() == "Postgraduate":
                    self.course_combo['values'] = ("Select", "M.Sc. in Mathematics")
                elif self.programme_combo.get() == "Research":
                    self.course_combo['values'] = ("Select","Ph.D. Applied Sciences")
            else:
                self.course_combo['value'] = (" ")
            self.course_combo.current(0)

        programme_label = Label(course_frame, text="Programme", font=("times new roman", 12, "bold"), bg="white", width=10)
        programme_label.grid(row=0, column=2, padx=10, pady=5)
        self.programme_combo = ttk.Combobox(course_frame, state="readonly", textvariable=self.var_prog,font=("times new roman", 10), width=25)
        self.programme_combo['values'] = ("Select","Undergraduate", "Postgraduate", "Research")
        self.programme_combo.current(0)
        self.programme_combo.grid(row=0, column=3, padx=10, pady=5)

        course_label = Label(course_frame, text="Course", font = ("times new roman", 12, "bold"), bg="white", width=10)
        course_label.grid(row=1, column=0, padx=10, pady=5)  
        self.course_combo = ttk.Combobox(course_frame, state="readonly", textvariable=self.var_course,font=("times new roman", 10), width=25)
        self.course_combo.grid(row=1, column=1, padx=10, pady=5)
        self.programme_combo.bind("<<ComboboxSelected>>", course_options)
        self.dept_combo.bind("<<ComboboxSelected>>", course_options)

        year_label = Label(course_frame, text = "Year", font= ("times new roman", 12, "bold"), bg="white", width=10)
        year_label.grid(row=1, column=2, padx=10,pady=5)
        year_combo = ttk.Combobox(course_frame, state="readonly", textvariable=self.var_year, font=("times new roman", 10), width=25)
        year_combo["values"] = ("Select", "2016", "2017", "2018", "2019","2020","2021")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=10, pady=5)

        #PERSONAL DETAILS
        info_frame = LabelFrame(left_frame, text = "Personal Details", font=("times new roman", 12, "bold"), bd=2, bg="white", relief=RIDGE)
        info_frame.place(x=5, y=240, width=702, height=230)

        fname_label = Label(info_frame, text="First name",  font=("times new roman", 12, "bold"), bg="white", width=10)
        fname_label.grid(row=0, column=0, padx=10, pady=5)
        fname_entry = ttk.Entry(info_frame, font=("times new roman", 10), width=28, textvariable=self.var_fname)
        fname_entry.grid(row=0, column=1, padx=10, pady=5)

        lname_label = Label(info_frame, text="Last name", font=("times new roman", 12, "bold"), bg="white", width=10)
        lname_label.grid(row=0, column=2, padx=10, pady=5)
        lname_entry = ttk.Entry(info_frame, font=("times new roman", 10), textvariable=self.var_lname, width=28)
        lname_entry.grid(row=0, column=3, padx=10, pady=5)

        roll_num_label = Label(info_frame, text="Roll number", font=("times new roman", 12, "bold"), bg="white", width=10)
        roll_num_label.grid(row=1, column=0, padx=10, pady=5)
        roll_num_entry = ttk.Entry(info_frame, font=("times new roman", 10), textvariable=self.var_roll, width=28)
        roll_num_entry.grid(row=1, column=1, padx=10, pady=5)
        
        dob_label = Label(info_frame, text="D.O.B.", font= ("times new roman", 12, "bold"), bg="white", width=10)
        dob_label.grid(row=1, column=2, padx=10, pady=5)
        cal = DateEntry(info_frame, width=25, background='#a8403d',textvariable=self.var_dob,
                        foreground='white', borderwidth=2)
        cal.grid(row=1, column=3, padx=10, pady=5)
        #cal.bind("<<DateEntrySelected", check_date)

        gender_label = Label(info_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white", width=10)
        gender_label.grid(row=2, column=0, padx=10, pady=5)
        gender_combo = ttk.Combobox(info_frame, state="readonly", font = ("times new roman",10), width=25, textvariable=self.var_gender)
        gender_combo['values'] = ("Select","Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5)

        email_label = Label(info_frame, text="Email", font=("times new roman", 12, "bold"), bg="white", width=10)
        email_label.grid(row=2, column=2, padx=10, pady=5)
        email_entry = ttk.Entry(info_frame, font=("times new roman", 10), width=28, textvariable=self.var_email)
        email_entry.grid(row=2, column=3, padx=10, pady=5)

        phone_label = Label(info_frame, text="Phone no.", font=("times new roman", 12, "bold"), bg="white", width=10)
        phone_label.grid(row=3, column=0, padx=10, pady=5)
        phone_entry = ttk.Entry(info_frame, font=("times new roman", 10), width=28, textvariable=self.var_phone)
        phone_entry.grid(row=3, column=1, padx=10, pady=5)

        father_label = Label(info_frame, text="Father's name", font=("times new roman", 12, "bold"), bg="white", width=10)
        father_label.grid(row=3, column=2, padx=10, pady=5)
        father_entry = ttk.Entry(info_frame, font=("times new roman", 10), width=28, textvariable=self.var_father)
        father_entry.grid(row=3, column=3, padx=10, pady=5)

        address_label = Label(info_frame, text="Address", font=("times new roman", 12, "bold"), bg="white", width=10)
        address_label.grid(row=4, column=0, padx=10, pady=5)
        address_entry = ttk.Entry(info_frame, font=("times new roman", 10), width=80, textvariable=self.var_address)
        address_entry.grid(row=4, column=1, padx=10, pady=5, columnspan = 3)
        
        self.var_photo = tk.StringVar()
        take_btn = Radiobutton(info_frame, text = "Take Photo Sample", variable = self.var_photo, value="Yes", bg="white",tristatevalue="x")
        take_btn.grid(row=5, column=0, padx=10, pady=5)
        no_sample_btn = Radiobutton(info_frame, text = "No Photo Sample", variable=self.var_photo, value="No", bg="white",tristatevalue="x")
        no_sample_btn.grid(row=5, column=2, padx=10, pady=5)

        #buttons frame
        btn_frame=Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=480, height=100, width=702)

        save_button = Button(btn_frame, text = "Save", font= ("times new roman",12,"bold"), 
                            bg="#a8403d", fg="white", width=19, command=self.add_data, cursor="hand2")
        save_button.grid(row=0, column=0, pady=10)

        update_button = Button(btn_frame, text = "Update", font= ("times new roman",12,"bold"),
                                cursor="hand2", bg="#a8403d", fg="white", width=18,command=self.update_data)
        update_button.grid(row=0, column=1)

        delete_button = Button(btn_frame, text = "Delete", font= ("times new roman",12,"bold"), 
                                cursor="hand2",bg="#a8403d", fg="white", width=18, command=self.delete_data)
        delete_button.grid(row=0, column=2)

        reset_button = Button(btn_frame, text = "Reset", font= ("times new roman",12,"bold"), 
                                cursor="hand2", bg="#a8403d", fg="white", width=18, command=self.reset_data)
        reset_button.grid(row=0, column=3)

        take_sample_button = Button(btn_frame, text = "Take Photo Sample", font= ("times new roman",12,"bold"), 
                                    cursor="hand2", bg="#a8403d", fg="white", width=38, command=self.take_photo_sample)
        take_sample_button.grid(row=1, column=0, columnspan=2)
        update_sample_button = Button(btn_frame, text = "Reset Photo Sample", font= ("times new roman",12,"bold"), 
                                        cursor="hand2", bg="#a8403d", fg="white", width=37)
        update_sample_button.grid(row=1, column=2, columnspan=2)

        #right level frame
        right_frame = LabelFrame(frame, bd=2, relief=RIDGE, bg="white", text = "Student Details", font=("times new roman", 18,"bold"))
        right_frame.place(x=760, y=10, width = 715, height = 620)

        student_2_img = Image.open("student2.jpg")
        student_2_img = student_2_img.resize((700,150), Image.ANTIALIAS)
        self.student_2_img = ImageTk.PhotoImage(student_2_img)
        right_frame_img = Label(right_frame, image=self.student_2_img)
        right_frame_img.place(x=5, y=0, width=702, height=150)


        search_frame = LabelFrame(right_frame, text = "Search Student", font=("times new roman", 12, "bold"), bd=2, bg="white", relief=RIDGE)
        search_frame.place(x=5, y=135, width=702, height=75)
        search_label = Label(search_frame, text="Search by :", font=("times new roman", 12, "bold"), bg="#a8403d", fg="white", width=10)
        search_label.grid(row=0, column=0, padx=10, pady=5)
        search_combo = ttk.Combobox(search_frame, state="readonly", font=("times new roman", 10), width=18, textvariable=self.var_searchby)
        search_combo['values'] = ("Select","RollNo", "PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5)
        search_entry = ttk.Entry(search_frame, font=("times new roman", 10), width=18, textvariable=self.var_search)
        search_entry.grid(row=0, column=2, padx=5, pady=5)
        search_button = Button(search_frame, text = "Search", font= ("times new roman",12, "bold"), 
                                cursor="hand2", bg="#a8403d", fg="white", width=15, command=self.search_data)
        search_button.grid(row=0, column=3, padx=5, pady=5)
        show_all_button = Button(search_frame, text = "Show All", font= ("times new roman",12, "bold"), 
                                cursor="hand2",bg="#a8403d", fg="white", width=15, command=self.get_data)
        show_all_button.grid(row=0, column=4, padx=5, pady=5)

        back_img = Image.open("back.png")
        back_img=back_img.resize((50,50),Image.ANTIALIAS)
        self.back_img = ImageTk.PhotoImage(back_img)
        back_btn = Button(right_frame, image=self.back_img, text="BACK", font=("times new roman", 22), 
                          bg="white", fg="#a8403d", compound=LEFT, cursor="hand2", command=self.root.destroy)
        back_btn.place(x=560, y=520)

        #------------TABLE------------------
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=220, width=702, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("school", "prog", "course", "year", "fname", "lname", "roll", 
                                        "dob", "gender", "email", "phone", "father", "address", "photo"), xscrollcommand = scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("school", text="School")
        self.student_table.heading("prog", text="Programme")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("fname", text="First Name")
        self.student_table.heading("lname", text="Last Name")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("father", text="Father's Name")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("school", width=100)
        self.student_table.column("prog", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("fname", width=100)
        self.student_table.column("lname", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("father", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.get_data()
    
        #self.student_table.tag_configure('odd', background="red")
        
    

     #-----------------ADD TO DATBASE----------------------   
    def add_data(self):
        if (self.var_school.get()=="Select" or self.var_prog.get()=="Select" or self.var_course.get()=="Select" 
        or self.var_course.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_roll.get()==""
        or self.var_gender.get()=="Select" or self.var_email=="" or self.var_phone==" " or self.var_father.get()==""
        or self.var_address.get()=="" or self.var_photo.get()=="" or self.var_dob==""):
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif not(all(i.isalpha() for i in self.var_fname.get())) or not(all(i.isalpha() for i in self.var_lname.get())) :
            messagebox.showerror("Error!", "Name should only contain alphabets")
        elif len(self.var_phone.get())!=10 or not(all(d.isdigit() for d in self.var_phone.get())):
               messagebox.showerror("Error!", "Invalid phone number!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_school.get(), 
                self.var_prog.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_roll.get(),
                self.var_dob.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_father.get(),
                self.var_address.get(),
                self.var_photo.get()
                ))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("success", "Details Added Successfully!", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent = self.root)


    #------------------------FETCH FROM DATABASE-------------------------------
    def get_data(self):
        conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        #if (len(data)!=0):
        self.student_table.delete(*self.student_table.get_children())
        for d in data:
            self.student_table.insert("", END,values=d)
        conn.commit()
        conn.close()

    #---------------------GET CURSOR--------------------------------
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_school.set(data[0]), 
        self.var_prog.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_fname.set(data[4]),
        self.var_lname.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_father.set(data[11]),
        self.var_address.set(data[12]),
        self.var_photo.set(data[13])

    #------------------ UPDATE DATA-----------------------------
    def update_data(self):
        if (self.var_school.get()=="Select" or self.var_prog.get()=="Select" or self.var_course.get()=="Select" 
        or self.var_course.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_roll.get()==""
        or self.var_gender.get()=="Select" or self.var_email=="" or self.var_phone==" " or self.var_father.get()==""
        or self.var_address.get()=="" or self.var_photo.get()=="" or self.var_dob==""):
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Are you sure you want to update?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set School=%s, Programme=%s, Course=%s, Year=%s, FirstName=%s, LastName=%s, Dob=%s, Gender=%s, Email=%s, PhoneNo=%s, FatherName=%s, Address=%s, PhotoSample=%s where RollNo=%s",(
                        self.var_school.get(), 
                        self.var_prog.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_father.get(),
                        self.var_address.get(),
                        self.var_photo.get(),
                        self.var_roll.get()
                    ))
                else:
                    if not update:
                      return
                messagebox.showinfo("Success","Student details successfully updated!", parent=self.root)
                self.reset_data()
                conn.commit()
                self.get_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)


    #------------------------DELETE DATA---------------------------------------
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error", "Enter Roll number!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Are you sure you want to delete this record?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
                    my_cursor = conn.cursor()
                    del_command = "delete from student where RollNo=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(del_command, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted Student details!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!", f"Due to:{str(es)}", parent=self.root) 

    #----------------------------RESET-----------------------------------
    def reset_data(self):
        self.var_school.set("Select"), 
        self.var_prog.set("Select"),
        self.var_course.set(""),
        self.var_year.set("Select"),
        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_gender.set("Select"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_father.set(""),
        self.var_address.set(""),
        self.var_photo.set("")

    #-------------------PHOTO SAMPLES--------------------
    def take_photo_sample(self):
        if (self.var_school.get()=="Select" or self.var_prog.get()=="Select" or self.var_course.get()=="Select" 
        or self.var_course.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_roll.get()==""
        or self.var_gender.get()=="Select" or self.var_email=="" or self.var_phone==" " or self.var_father.get()==""
        or self.var_address.get()=="" or self.var_photo.get()=="" or self.var_dob==""):
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
                my_cursor = conn.cursor()
                r = self.var_roll.get()
                rnum = str(r)
                #sql = "select * from student where RollNo=%s"
                #my_cursor.execute(sql, (rnum,))
                #result = my_cursor.fetchall()
                my_cursor.execute("update student set School=%s, Programme=%s, Course=%s, Year=%s, FirstName=%s, LastName=%s, Dob=%s, Gender=%s, Email=%s, PhoneNo=%s, FatherName=%s, Address=%s, PhotoSample=%s where RollNo=%s",(
                        self.var_school.get(), 
                        self.var_prog.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_father.get(),
                        self.var_address.get(),
                        self.var_photo.get(),
                        self.var_roll.get()
                    ))
                conn.commit()
                self.get_data()
                #self.reset_data()
                conn.close()

                #--------------- Load predefined data on face frontals from opencv----------------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                # Parent Directory path
                parent_dir = "images/"
                # Path
                path = os.path.join(parent_dir, rnum)
                os.mkdir(path)
                def crop_face(img):
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray_img,1.3,5)  #taking scaling factor as 1.3 and minimum neightbours=5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]                            
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
            
                img_id=0
                while True: #infinite loop
                    ret, my_frame = cap.read()
                    if crop_face(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(crop_face(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    face = cv2.fastNlMeansDenoising(face,None,10,21,7)
                    maxi = np.amax(face)
                    mini = np.amin(face)
                    intensity_range = maxi - mini
                    face = ((face.astype('float64') - mini) * 255 / intensity_range).astype('uint8')
                    file_path = "photos/user."+rnum+"."+str(img_id)+".jpg"
                    file_path = path+str('/')+str(img_id)+".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("cropped face", face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)


    def search_data(self):
        if self.var_search.get()=="" or self.var_searchby.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Kanika@2192000',database='attendance')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_searchby.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    #if rows==None:
                    #    messagebox.showerror("Error","Data Not Found",parent=self.root)
                    #    conn.commit()  
                else:
                    messagebox.showerror("Error","Data Not Found",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()