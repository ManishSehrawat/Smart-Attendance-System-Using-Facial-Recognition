from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter.font as f
import numpy as np
#import mtcnn
import os
from PIL import Image
#ImageOps
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
#from mtcnn.mtcnn import MTCNN
#from sklearn.externals import joblib
import joblib
#from numpy import load
#from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
#from keras.models import load_model
import pickle
#from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import Normalizer
#from sklearn.svm import SVC
#from sklearn.model_selection import StratifiedKFold
#from keras_facenet import FaceNet
import webbrowser

class Train:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.iconbitmap('logo.ico')
        self.root.attributes("-fullscreen", True)

        bg_img=Image.open("train_bg.png")
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
        
        train_lbl = Label(bg_lbl, text ="Click the button to start training..", font=("times new roman",17, "bold"), bg='#00061a', fg='#54c1e6')
        train_lbl.place(x=130, y=280)
        myFont = f.Font(size=27, family="Times New Roman")
        train_btn = Button(self.root, text = "START TRAINING MODEL", relief=RAISED,
                            cursor="hand2", bg="#54c1e6", fg="#022051", command=self.train_model)
        train_btn.place(x=130,y=450)
        train_btn['font'] = myFont
    
    def train_model(self):
        directory = ("images")
        path = [os.path.join(directory,file)+"\\" for file in os.listdir(directory)]
        faces=[]
        ids = []
        for roll in path:
            for image in os.listdir(roll):
                img_path = os.path.join(roll, image)
                img = Image.open(img_path).convert('L')
                img_arr = np.array(img, 'uint8')
                id = str(os.path.split(os.path.split(roll)[0])[1])
                faces.append(img_arr)
                ids.append(id)
                cv2.imshow("Training",img_arr)
                cv2.waitKey(1)==13
        label_encoder = LabelEncoder()
        ids = label_encoder.fit_transform(ids)
        np.save('classes.npy', label_encoder.classes_)
        ids=np.array(ids)

        #--------------------------------- training and saving the model ---------------------------------
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(faces,ids)
        model.write("model.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

