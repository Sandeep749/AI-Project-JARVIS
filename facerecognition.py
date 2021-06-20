

import cv2 
import numpy as np
from PIL import Image
import os
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import speech_recognition as sr
import pyttsx3
import requests


window = tk.Tk()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


window.title("Face recognition system")
lW=tk.Label(window,text="Create Account",font=("Algerian",20))
lW.grid(column=1,row=0)
l1=tk.Label(window,text="Name",font=("Algerian",20))
l1.grid(column=0,row=1)
t1=tk.Entry(window,width=50,bd=5)
t1.grid(column=1,row=1)

l2=tk.Label(window,text="Email",font=("Algerian",20))
l2.grid(column=0,row=2)
t2=tk.Entry(window,width=50,bd=5)
t2.grid(column=1,row=2)

l3=tk.Label(window,text="Age",font=("Algerian",20))
l3.grid(column=0,row=3)
t3=tk.Entry(window,width=50,bd=5)
t3.grid(column=1,row=3)

l4=tk.Label(window,text="Address",font=("Algerian",20))
l4.grid(column=0,row=4)
t4=tk.Entry(window,width=50,bd=5)
t4.grid(column=1,row=4)

speak("Welcome to face econition sytem.")
###########################################################################
################### For training of images seted on setData file ##########
def train_classifier():
     data_dir="D:\\Sandeep\\J.A.R.V.I.S\\facerecognition-login-master\\dataSet"
     path = [ os.path.join(data_dir,f) for f in os.listdir(data_dir)]
     faces = []
     ids = []
     for image in path:
         img= Image.open(image).convert('L')
         imageNp= np.array(img,'uint8')
         id = int(os.path.split(image)[1].split(".")[1])
         faces.append(imageNp)
         ids.append(id)
     ids=np.array(ids)
     clf= cv2.face.LBPHFaceRecognizer_create()
     clf.train(faces,ids)
     clf.write("classifier.xml")
     messagebox.showinfo('Result','data set and train completed')

# b1=tk.Button(window,text="Training",font=("Algerian",20),bg="blue",fg="white",command=train_classifier)
# b1.grid(column=0,row=6)


################################################################################
########## I am commenting this because code shifted  on firstscreeen.py #######
# def detect_face():
#     def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#         coords = []

#         for(x,y,w,h) in features:
#             cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
#             id,pred = clf.predict(gray_image[y:y+h,x:x+w])
#             confidence = int(100*(1-pred/300))
                
            
#             mydb=mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd="",
#             database="Face_authorized_user"
#             )
#             mycursor=mydb.cursor()
#             mycursor.execute("select name from my_table where id="+str(id))
#             s = mycursor.fetchone()
#             s = ''+''.join(s)
            
#             if confidence>74:
#                 cv2.putText(img,s,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)   
#             else:
#                 cv2.putText(img,"UNKNOWN",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
            
#     def recognize(img,clf,faceCascade):
#         #for drawind squire on face
#         coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
#         return img

#     faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     clf = cv2.face.LBPHFaceRecognizer_create()
#     clf.read("classifier.xml")

#     video_capture =  cv2.VideoCapture(0)

#     while True:
#         ret,img = video_capture.read()
#         img=  recognize(img,clf,faceCascade)
#         cv2.imshow("face detection",img)

#         if cv2.waitKey(1)==13:
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()

#############################################################################


# b2=tk.Button(window,text="Detect face",font=("Algerian",20),bg="green",fg="white",command=detect_face)
# b2.grid(column=1,row=6)

speak("I am jarvish I will act as guid for your upcoming process")
#############################################################################
########### for genrating data of images       ##############################
def genrate_dataset():
    if(t1.get()=="" or t2.get()=="" or t3.get()==""):
        messagebox.showinfo('Result',"Please fill all the field")
    else:
       mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="",
       database="Face_authorized_user")
       mycursor=mydb.cursor()
       mycursor.execute("SELECT * from my_table")
       myresult=mycursor.fetchall()
       id=1
       for x in myresult:
         id=id+1
       sql="insert into my_table(id,Name,email,Age,Address) values(%s,%s,%s,%s,%s)"
       val=(id,t1.get(),t2.get(),t3.get(),t4.get())
       mycursor.execute(sql,val)
       mydb.commit()
       face_classifier = cv2.CascadeClassifier("D:\\Sandeep\\J.A.R.V.I.S\\facerecognition-login-master\\haarcascade_frontalface_default.xml")
       def face_cropped(img):
            gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            #scaling factor=1.3
            #Minimum neighbor = 5
            if faces is ():
                return None
            for(x,y,w,h) in faces:
                cropped_face=img[y:y+h,x:x+w]
            return cropped_face

       cap = cv2.VideoCapture(0)
       
            
       #id=1
       img_id=0
       speak("Please looked the camera, your face data genration process is started")

       while True:
        ret,frame = cap.read()
        if face_cropped(frame) is not None:
            img_id=img_id+1
            face = cv2.resize(face_cropped(frame),(200,200))
            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            
           # face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_path = "dataSet/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_path,face)
            
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),2)
            # 50,50 IS ORIGIN POINT FROM WHERE TEXT IS BE TO RETURN
            # FONT SCALE=1
            # THICKNESS = 2
          
            cv2.imshow('frame',face)
            # when we press enter or image id == 100 it will breake
            if cv2.waitKey(1)==13 or int(img_id)==100:
                break

       cap.release()
       
       cv2.destroyAllWindows()
       messagebox.showinfo('Result',"genrating dataset completed")
       train_classifier()
       #print("Collecting sample is completed .....")

#############################################################################
##################### Normal tkinter form for data recieving ################       
lb=tk.Label(window,text="             ",font=("Algerian",20))
lb.grid(column=0,row=5)
b3=tk.Button(window,text="set data",font=("Algerian",20),bg="pink",fg="black",command=genrate_dataset)
b3.grid(column=1,row=6)
window.geometry("600x400")
window.mainloop()
