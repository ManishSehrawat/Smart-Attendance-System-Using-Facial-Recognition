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
import csv
from tkinter import filedialog


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)
        

        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_course=StringVar()
        self.var_school=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()


        img1 = Image.open("records-left-img.png")
        img1 = img1.resize((450,200), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.img1) 
        f_lbl.place(x=350,y=0,width=450,height=200)
        
        img2 = Image.open("student2.jpg")
        img2 = img2.resize((600,200), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)
        
        
        f_lbl=Label(self.root,image=self.img2) 
        f_lbl.place(x=800,y=0,width=600,height=200)
        
        img3 = Image.open("records-left-img.png")
        img3 = img3.resize((1530,710), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image = self.img3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
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
        quit_btn.place(x=1335,y=0,height=200, width=200)
        quit_btn.bind("<Enter>", lambda e: quit_btn.config(bg='#DCDCDC'))
        quit_btn.bind("<Leave>", lambda e: quit_btn.config( bg='white'))
   
        
        def visitSite():
            url="https://www.ncuindia.edu/"
            webbrowser.open(url)

        logo_img=Image.open("logo.png")
        logo_img=logo_img.resize((300,130),Image.ANTIALIAS)
        self.logo_img=ImageTk.PhotoImage(logo_img)
        logo_btn=Button(self.root,image=self.logo_img, bg='white', relief=RAISED, command=visitSite, cursor="hand2")
        logo_btn.place(x=0,y=0,height=200, width=350)
        logo_btn.bind("<Enter>", lambda e: logo_btn.config(bg='#DCDCDC'))
        logo_btn.bind("<Leave>", lambda e: logo_btn.config( bg='white'))

        head_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35, "bold"), bg='white', fg='#a8403d', padx=50)
        head_lbl.place(x=0,y=0, width=1530, height=45)
        
        frame = Frame(bg_img, bd=2, bg="white")
        frame.place(x=15, y=55, width=1500, height=660)

        #left level frame
        left_frame = LabelFrame(frame, bd=2, relief=RIDGE, bg="white", text = "Student Attendance Details", font=("times new roman", 18,"bold"))
        left_frame.place(x=15, y=10, width = 715, height = 620)
        
        img_left = Image.open("left-frame-img.png") 
        img_left=img_left.resize((700,180),Image.ANTIALIAS) 
        
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(left_frame,image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=700,height = 180) 
        
        left_inside_frame = Frame(left_frame,bd=2,relief = RIDGE,bg="white")
        left_inside_frame.place(x=15,y=190,width=680,height=200)
        
        name_label = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"), bg="white", width=10)
        name_label.grid(row=0, column=0, padx=10, pady=10,sticky = W)
        
        name_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_name)
        name_entry.grid(row=0, column=1 , padx=10, pady=10,sticky = W)

        roll_label = Label(left_inside_frame, text="Roll Number", font=("times new roman", 12, "bold"), bg="white", width=10)
        roll_label.grid(row=0, column=2, padx=10, pady=10,sticky = W)
        
        roll_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_roll)
        roll_entry.grid(row=0, column=3 , padx=10, pady=10,sticky = W)

        course_label = Label(left_inside_frame, text="Course", font=("times new roman", 12, "bold"), bg="white", width=10)
        course_label.grid(row=1, column=0, padx=10, pady=10,sticky = W)
        
        course_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_course)
        course_entry.grid(row=1, column=1 , padx=10, pady=10,sticky = W)
        
        school_label = Label(left_inside_frame, text="School", font=("times new roman", 12, "bold"), bg="white", width=10)
        school_label.grid(row=1, column=2, padx=10, pady=10,sticky = W)
        
        school_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_school)
        school_entry.grid(row=1, column=3 , padx=10, pady=10,sticky = W)
        
        time_label = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"), bg="white", width=10)
        time_label.grid(row=2, column=0, padx=10, pady=10,sticky = W)
        
        time_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_time)
        time_entry.grid(row=2, column=1 , padx=10, pady=10,sticky = W)
        
        date_label = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"), bg="white", width=10)
        date_label.grid(row=2, column=2, padx=10, pady=10,sticky = W)
        
        date_entry = ttk.Entry(left_inside_frame, font=("times new roman", 10), width=28, textvariable=self.var_date)
        date_entry.grid(row=2, column=3 , padx=10, pady=10)
        
        status_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        status_label.grid(row=3, column=0, pady=10,sticky = W)
        
        status_combo = ttk.Combobox(left_inside_frame, state="readonly", font = ("times new roman",10), width=25, textvariable=self.var_attendance)
        status_combo['values'] = ("Select","Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, pady=10)
        
        #buttons
        btn_frame=Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=28, y=450, height=35, width=620)

        import_button = Button(btn_frame, text = "Import CSV", font= ("times new roman",12,"bold"), 
                            bg="#a8403d", fg="white", width=16,  cursor="hand2",command = self.import_csv)
        import_button.grid(row=0, column=0)

        export_button = Button(btn_frame, text = "Export CSV", font= ("times new roman",12,"bold"),
                                cursor="hand2", bg="#a8403d", fg="white", width=16,command = self.export_csv)
        export_button.grid(row=0, column=1)

        update_button = Button(btn_frame, text = "Update", font= ("times new roman",12,"bold"), 
                                cursor="hand2",bg="#a8403d", fg="white", width=16, command = self.action)
        update_button.grid(row=0, column=2)

        reset_button = Button(btn_frame, text = "Reset", font= ("times new roman",12,"bold"), 
                                cursor="hand2", bg="#a8403d", fg="white", width=16, command=self.reset)
        reset_button.grid(row=0, column=3)
        
        

        right_frame = LabelFrame(frame, bd=2, relief=RIDGE, bg="white", font=("times new roman", 18,"bold"))
        right_frame.place(x=750, y=10, width = 725, height = 620)
        
        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg="white", text = "Student Attendance Details", font=("times new roman", 18,"bold"))
        table_frame.place(x=5, y=5, width = 715, height = 455)
        

        back_img = Image.open("back.png")
        back_img=back_img.resize((50,50),Image.ANTIALIAS)
        self.back_img = ImageTk.PhotoImage(back_img)
        back_btn = Button(right_frame, image=self.back_img, text="BACK", font=("times new roman", 22), 
                          bg="white", fg="#a8403d", compound=LEFT, cursor="hand2", command=self.root.destroy)
        back_btn.place(x=560, y=520)


        # ======================= scroll bar table ==================
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("name","roll","course","school","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("course",text="Course")
        self.AttendanceReportTable.heading("school",text="School")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"] ="headings"
        
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("course",width=100)
        self.AttendanceReportTable.column("school",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand = 1)
        
        self.AttendanceReportTable.bind('<ButtonRelease>', self.get_cursor)

    #-------------------------fetching data-------------------------------
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    

    #import csv
    def import_csv(self):
        global my_data
        my_data = []
        my_data.clear()
        global fln
        fln = filedialog.askopenfilename(initialdir=os.path.join(os.getcwd(),"record"), title="Open CSV", filetypes=(("CSV File", "*.csv"),("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)
    
    #export csv
    def export_csv(self):
        try:
            global my_data
            if len(my_data)==0:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False
            #fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data exported successfully to "+os.path.basename(fln)+"!")
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_name.set(row[0])
        self.var_roll.set(row[1])
        self.var_course.set(row[2])
        self.var_school.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendance.set(row[6])

    #export update
    def action(self):
        name=self.var_name.get()
        roll=self.var_roll.get()
        course=self.var_course.get()
        school=self.var_school.get()
        time=self.var_time.get()
        date=self.var_date.get()
        attendance=self.var_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=DictWriter(f,fieldnames=(["Name","Roll","Course","School","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "Name":name,
                "Roll":roll,
                "Course":course,
                "School":school,
                "Time":time,
                "Date":date,
                "Attendance":attendance 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    def reset(self):
        self.var_name.set("")
        self.var_roll.set("")
        self.var_course.set("")
        self.var_school.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__=="__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()