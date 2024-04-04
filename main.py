from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from student import Student
import os
from train import Train
from face_recognise import Face_Recognition
from attendance import Attendance
from datetime import datetime

def main():
    win = Tk()
    app = Face_Recognition_System(win)
    win.winloop()
    
########## 

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root      
        self.root.geometry("1273x650+0+0")
        self.root.title("Face_Recognition_System")
        
        #first image
        img1 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\tint1.jpg")
        img1 = img1.resize((500,220), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=470,height=130)

        # Second image
        img2 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\face.jpg")
        img2 = img2.resize((500,220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=480,height=130)

        #Third image
        img3 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1028266408-612x612.jpg")
        img3 = img3.resize((500,220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=800,y=0,width=480,height=130)
        
        #bg image
        imgbg = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\planebg.jpg")
        imgbg = imgbg.resize((1273,650), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=130,width=1273,height=650)
        
        # title
        title_lbl = Label(bg_img, text = "AUTOMATED FACE ATTENDANCE SYSTEM ", font=("times new roman",25,"bold"),bg ="white", fg = "black")
        title_lbl.place(x=0,y=5, width = 1270, height=45)
        
        ## back button
        back_btn = Button(bg_img,text = "Back",  command=self.back,width=14,font=("times new romen",15,"bold"),bg = "red",fg="white")
        back_btn.place(x=1165,y=10,width=90,height=25)
        
        
        # -------- time ---------
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl=Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        
        #student button
        img4 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\pexels-photo-5676744.jpeg")
        img4 = img4.resize((150,150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4,command= self.student_details,cursor="hand2")
        b1.place(x=350,y=80,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Student Details",command= self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=350,y=200,width=150,height=30)
        
        #Detect face button
        img5 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1352856539-612x612.jpg")
        img5 = img5.resize((150,150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=550,y=80,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=550,y=200,width=150,height=30)
        
        
        #Attendance face button
        img6 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1483190023-1024x1024.jpg")
        img6 = img6.resize((150,150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=750,y=80,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=750,y=200,width=150,height=30)
        
        #Train data button
        img8 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\2293aa6eb591e98ccb3f74fbbb3aa30d.jpg")
        img8 = img8.resize((151,146), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=350,y=250,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=350,y=380,width=150,height=30)
        
        #Photos button
        img9 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\photos.jpeg")
        img9 = img9.resize((150,150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=550,y=250,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=550,y=380,width=150,height=30)
        
        #Exit button
        img10 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\exitbtn(2).jpeg")
        img10 = img10.resize((150,150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.iExit)
        b1.place(x=750,y=250,width=150,height=150)
        
        b1_1 = Button(bg_img, text = "Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg ="darkblue", fg = "white")
        b1_1.place(x=750,y=380,width=150,height=30)
        
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if  self.iExit > 0:
            self.root.destroy()
        else:
            return
    
    def back(self):
        self.root.destroy()
        
        
    def open_img(self):
        os.startfile("Attendance_system\data")
        
    # function buttons=========
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    



if __name__ == "__main__":                                          
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()