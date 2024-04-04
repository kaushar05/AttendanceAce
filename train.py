from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1273x650+0+0")
        self.root.title("Training Images")
        
        
        title_lbl = Label(self.root,text = "TRAIN DATA SET",font=("times new roman",25,"bold"),bg ="white", fg = "Black")
        title_lbl.place(x=0,y=0, width = 1272, height=45)
        
        ## back button
        back_btn = Button(self.root,text = "Back", command=self.back, width=14,font=("times new romen",15,"bold"),bg = "red",fg="white")
        back_btn.place(x=1160,y=10,width=80,height=25)
         
        #top image        
        img_top = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1465476073-612x612.jpg")
        img_top = img_top.resize((1300,650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1300,height=590)
        
        #button
        b1_1 = Button(self.root,text="Click here to TRAIN DATA", cursor="hand2",command=self.train_classifier,font=("times new roman",25,"bold" ),bg="dark green", fg="white")
        b1_1.place(x=800,y=410,width=450,height=50)
        
    def back(self):
        self.root.destroy()
        

    def train_classifier(self):
        data_dir = ("C:\Shamina\projects\Flask_project\Attendance_system\data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #converted in grey scale image
            imageNp= np.array(img,'uint8')  #uint8 -> its a datatype
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        ######### train the classifier ##########
        
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("C:\Shamina\projects\Flask_project\Attendance_system\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed!!")
        
            
    
    
if __name__ == "__main__":                                          
    root=Tk()
    obj=Train(root)
    root.mainloop()