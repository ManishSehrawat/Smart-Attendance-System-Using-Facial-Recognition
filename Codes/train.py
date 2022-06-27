from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter.font as f
import numpy as np
import mtcnn
import cv2
from os import listdir
from os.path import isdir
from PIL import Image,ImageOps
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN
#from sklearn.externals import joblib
import joblib
from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
from keras.models import load_model
import pickle
from numpy import load
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from keras_facenet import FaceNet

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
        # extract a single face from a given photograph
        def extract_face(filename, required_size=(160, 160)):
            # load image from file
            image = Image.open(filename)
            # convert to RGB, if needed
            image = image.convert('RGB')
            # convert to array
            pixels = asarray(image)
            # create the detector, using default weights
            detector = MTCNN()
            # detect faces in the image
            results = detector.detect_faces(pixels)
            # extract the bounding box from the first face
            x1, y1, width, height = results[0]['box']
            # bug fix
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            # extract the face
            face = pixels[y1:y2, x1:x2]
            # resize pixels to the model size
            image = Image.fromarray(face)
            image = image.resize(required_size)
            face_array = asarray(image)
            return face_array
        
        # load images and extract faces for all images in a directory
        def load_faces(directory):
            faces = list()
            # enumerate files
            i = 0
            for filename in listdir(directory):
                # path
                path = directory + filename
                # get face
                face = extract_face(path)
                # store
                faces.append(face)
                i = i+1
                if(i==2):
                    break
            return faces
         
        # load a dataset that contains one subdir for each class that in turn contains images
        def load_dataset(directory):
            X, y = list(), list()
            # enumerate folders, on per class
            for subdir in listdir(directory):
                # path
                path = directory + subdir + '/'
                # skip any files that might be in the dir
                if not isdir(path):
                    continue
                # load all faces in the subdirectory
                faces = load_faces(path)
                # create labels
                labels = [subdir for _ in range(len(faces))]
                # summarize progress
                print('>loaded %d examples for class: %s' % (len(faces), subdir))
                # store
                X.extend(faces)
                y.extend(labels)
            return asarray(X), asarray(y)
         
            
        # calculate a face embedding for each face in the dataset using facenet
        
        
        # get the face embedding for one face
        def get_embedding(model, face_pixels):
            # scale pixel values
            face_pixels = face_pixels.astype('float32')
            # standardize pixel values across channels (global)
            mean, std = face_pixels.mean(), face_pixels.std()
            face_pixels = (face_pixels - mean) / std
            # transform face into one sample
            samples = expand_dims(face_pixels, axis=0)
            # make prediction to get embedding
            yhat = model.predict(samples)
            return yhat[0]
        def pre_process(data):
            trainX, trainy = data['arr_0'], data['arr_1']
            print('Dataset: train=%d' % (trainX.shape[0]))
            # normalize input vectors
            in_encoder = Normalizer(norm='l2')
            trainX = in_encoder.transform(trainX)
            # label encode targets
            out_encoder = LabelEncoder()
            out_encoder.fit(trainy)
            trainy = out_encoder.transform(trainy)
            return trainX,trainy
            
        def main():
            trainX, trainy = load_dataset('images/')
            print(trainX.shape, trainy.shape)
            savez_compressed('5-celebrity-faces-dataset.npz', trainX, trainy)
            data = np.load('5-celebrity-faces-dataset.npz')
            trainX, trainy = data['arr_0'], data['arr_1']
            print('Loaded: ', trainX.shape, trainy.shape)
            # load the facenet model
            #-------------------------------------------------------------------------------------------------------------------------------
            #model = load_model('facenet_keras.h5')
            model = FaceNet()
            print('Loaded Model')
            # convert each face in the train set to an embedding
            newTrainX = list()
            for face_pixels in trainX:
                #embedding = get_embedding(model, face_pixels)
                embedding = model.extract(image, threshold=0.95)
                newTrainX.append(embedding)
            newTrainX = asarray(newTrainX)
            print(newTrainX.shape)
            # save arrays to one file in compressed format
            savez_compressed('5-celebrity-faces-embeddings.npz', newTrainX, trainy)
            data = load('5-celebrity-faces-embeddings.npz')
            trainX,train =  pre_process(data)
            model = SVC(kernel='linear', probability=True)
            
            skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=1)
            lst_accu_stratified = []
           
            for train_index, test_index in skf.split(trainX, trainy):
                x_train_fold, x_test_fold = trainX[train_index], trainX[test_index]
                y_train_fold, y_test_fold = trainy[train_index], trainy[test_index]
                # fit model
                model.fit(trainX, trainy)
                lst_accu_stratified.append(model.score(x_test_fold, y_test_fold))
            #Dump the Model
            print("The accuracy is ")
            print(sum(lst_accu_stratified)/len(lst_accu_stratified))
            joblib.dump(model, 'filename.pkl')
            print("The model is trained and dumped sucessfully")

        train_lbl = Label(bg_lbl, text ="Click the button to start training..", font=("times new roman",17, "bold"), bg='#00061a', fg='#54c1e6')
        train_lbl.place(x=130, y=280)
        myFont = f.Font(size=27, family="Times New Roman")
        train_btn = Button(self.root, text = "START TRAINING MODEL", relief=RAISED,
                            cursor="hand2", bg="#54c1e6", fg="#022051",command = main)
        train_btn.place(x=130,y=450)
        train_btn['font'] = myFont

   
      

if __name__=="__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()