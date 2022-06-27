from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as f
import cv2
import mysql.connector
from sklearn.preprocessing import LabelEncoder
import numpy as np
from time import strftime
import datetime
import os
import webbrowser

class Recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)

        bg_img=Image.open("recog_bg.png")
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


        back_img = Image.open("back.png")
        back_img=back_img.resize((50,50),Image.ANTIALIAS)
        self.back_img = ImageTk.PhotoImage(back_img)
        back_btn = Button(bg_lbl, image=self.back_img, text="BACK", font=("times new roman", 22, "bold"), 
                          bg="white", fg="#a8403d", compound=LEFT, cursor="hand2", command=self.root.destroy)
        back_btn.place(x=1350, y=650)
        back_btn.bind("<Enter>", lambda e: back_btn.config(bg='#DCDCDC'))
        back_btn.bind("<Leave>", lambda e: back_btn.config( bg='white'))


        head_lbl=Label(bg_lbl, text="STUDENT DETAILS MANAGEMENT SYSTEM", 
                        font=("times new roman",35, "bold"), bg='white', fg='#a8403d', padx=50)
        head_lbl.place(x=0,y=0, width=1530, height=45)


        recognition_lbl = Label(bg_lbl, text ="Click the button to mark your attendance..", font=("times new roman",17, "bold"), bg='#fc507d', fg='#022051')
        recognition_lbl.place(x=130, y=180)
        myFont = f.Font(size=27, family="Times New Roman")
        recognition_btn = Button(self.root, text = "FACE RECOGNITION", relief=RAISED,
                            cursor="hand2", bg="#54c1e6", fg="#022051", command=self.face_recognition)
        recognition_btn.place(x=250,y=350, height=350)
        recognition_btn['font'] = myFont

    
    label_encoder = LabelEncoder()
    label_encoder.classes_ = np.load('classes.npy')
    
    #---------------------------ATTENDANCE DATABASE-------------------------------
    
    def mark_attendance(self,student_name,roll,course,school):
        today = datetime.date.today()
        path = os.path.join("record",str(today))
        if not os.path.exists(path):
            os.mkdir(path)
        if school == "School of engineering":
            path = os.path.join(path,"engineering.csv")
        elif school== "School of law":
            path = os.path.join(path,"law.csv")
        elif school=="School of management":
            path = os.path.join(path,"management.csv")   
        elif school=="School of applied sciences":
            path=os.path.join(path,"sciences.csv")
        if not os.path.exists(path):
            #with open(path, 'a+'):
            with open(path, "w", newline="") as outfile:
                pass 
        with open(path,"r+",newline = "\n") as f:
            myDataList = f.readlines()
            roll_list = [] 
            for line in myDataList:
                entry = line.split((",")) 
                roll_list.append(entry[1]) 
            if(roll not in roll_list):
                now=datetime.datetime.now()
                d1=now.strftime("%d/%m/%Y") 
                dtString=now.strftime("%H:%M:%S") 
                f.writelines(f"{student_name},{roll},{course},{school},{dtString},{d1},Present\n") 
               

     #--------------------------FACE RECOGNITION-------------------------------
    def face_recognition(self):
        def draw_rectangle(img, classifier, scaleFactor, minNeighbors, color, text, clf):

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_img = cv2.fastNlMeansDenoising(gray_img,None,10,21,7)
            maxi = np.amax(gray_img)
            mini = np.amin(gray_img)
            intensity_range = maxi - mini
            gray_img = ((gray_img.astype('float64') - mini) * 255 / intensity_range).astype('uint8')
            features = classifier.detectMultiScale(gray_img,scaleFactor, minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 3)
                roll , predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))
                roll=self.label_encoder.inverse_transform([roll])[0]
                conn = mysql.connector.connect(host="localhost",user="root", password="Kanika@2192000",database="attendance")
                my_cursor = conn.cursor()

                my_cursor.execute("Select FirstName from student where RollNo=('%s')"%(roll))
                student_name = my_cursor.fetchone()
                student_name = "+".join(student_name)
                
                my_cursor.execute("Select RollNo from student where RollNo=('%s')"%(roll))
                roll = my_cursor.fetchone()
                roll = "+".join(roll)
                
                my_cursor.execute("Select Course from student where RollNo=('%s')"%(roll))
                course = my_cursor.fetchone()
                course = "+".join(course)
                
                                
                my_cursor.execute("Select School from student where RollNo=('%s')"%(roll))
                school = my_cursor.fetchone()
                school = "+".join(school)
              
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{str(roll)}", (x,y-100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Name:{student_name}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Name:{course}", (x,y-50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img,f"Name:{school}", (x,y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(student_name,roll,course,school)
                else:
                    cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img,f"Unknown face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord = [x,y,w,y]
            return coord


        def recognize_face(img, clf, faceCascade):
            coord = draw_rectangle(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("model.xml")

        video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        video_capture.set(3,1920)
        video_capture.set(4,920)
        while True:
            ret, img  = video_capture.read()
            img = recognize_face(img, clf, faceCascade)
            cv2.imshow("Recognizing face.....", img)
            if cv2.waitKey(33) == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj = Recognition(root)
    root.mainloop()