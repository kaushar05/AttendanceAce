from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1273x650+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl = Label(self.root,text = "FACE RECOGNITION",font=("times new roman",25,"bold"),bg ="white", fg = "green")
        title_lbl.place(x=0,y=0, width = 1272, height=45)
        
        ## back button
        back_btn = Button(self.root,text = "Back", command=self.back, width=14,font=("times new romen",15,"bold"),bg = "red",fg="white")
        back_btn.place(x=1160,y=15,width=80,height=25)
         
        
        #1st image
        img_top = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\bg.jpg")
        img_top = img_top.resize((540,560), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=540,height=560)
        
        #2nd image
        img_bottom = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((840,560), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=540,y=45,width=840,height=560)
        
        b1_1 = Button(self.root,text="Face Recognition", cursor="hand2", command= self.face_recog, font=("times new roman",15,"bold" ),bg="green", fg="white")
        b1_1.place(x=863,y=540,width=200,height=40)
        
        
        
    def back(self):
        self.root.destroy()    
    
        ###########Mark Attendance#############
    def markAttendence(self,i,r,n,d):
        with open("Attendance_system\shamina.csv","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_List=[]
            for line in mydataList:
                entry = line.split(",")
                name_List.append(entry[0])
            if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
            
        
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where student_id ="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll_no from student where student_id ="+str(id))
                r = my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where student_id ="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from student where student_id ="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)
                
                
                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_no:{r}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.markAttendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown face", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
            return coord
        
        
        def recognize(img, clf, faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1, 10, (255,25,255),"Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("C:\Shamina\projects\Flask_project\Attendance_system\haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("C:\Shamina\projects\Flask_project\Attendance_system\classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
            

    
        
if __name__ == "__main__":                                          
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()