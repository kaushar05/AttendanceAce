from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1273x650+0+0")
        self.root.title("Face Recognition System")
        
        ######### variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        #1st image
        img_top = Image.open(r"Attendance_system\images\Smart-Attendance-System-For-Schools.jpg")
        img_top = img_top.resize((500,100), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=500,height=100)
        
        #2nd image
        img_bottom = Image.open(r"Attendance_system\images\facial-recognition_0.jpg")
        img_bottom = img_bottom.resize((800,200), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=500,y=0,width=800,height=200)
        
        
        #bg image
        imgbg = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\planebg.jpg")
        imgbg = imgbg.resize((1273,650), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=100,width=1273,height=650)
        
        #title
        title_lbl = Label(bg_img, text = "ATTENDANCE MANAGEMENT", font=("times new roman",25,"bold"),bg ="white", fg = "darkgreen")
        title_lbl.place(x=0,y=0, width = 1270, height=37)
        
        ## back button
        back_btn = Button(bg_img,text = "Back", command=self.back, width=14,font=("times new romen",15,"bold"),bg = "red",fg="white")
        back_btn.place(x=1160,y=10,width=80,height=25)
     
        # Main frame
        main_frame = Frame(bg_img,bd=2,bg="white")#############
        main_frame.place(x=15,y=43,width=1234,height=600)
        
        #left side level frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Student Attendance Details", font=("times new romen",15,"bold"))
        Left_frame.place(x=10,y=2,width=620,height=495)
        
        img_left = Image.open(r"Attendance_system\images\inner-banner2.jpg")
        img_left = img_left.resize((700,300), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=611,height=200)
        
        Left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")#############
        Left_inside_frame.place(x=2,y=210,width=612,height=400)
        
        #labels and entry
        #attendance id
        attendanceId_lbl = Label(Left_inside_frame, text="AttendanceId:", font =("times new roman",12,"bold"),bg ="white")
        attendanceId_lbl.grid(row=0,column=0,padx=10, pady=5,sticky=W)
        
        attendanceId_entry = ttk.Entry(Left_inside_frame, width=20,textvariable=self.var_atten_id, font =("times new roman",12))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #roll
        Roll_lbl = Label(Left_inside_frame, text="Roll:", font =("times new roman",12,"bold"),bg ="white")
        Roll_lbl.grid(row=0,column=2,padx=4, pady=8)
        
        Roll_entry = ttk.Entry(Left_inside_frame, width=20,textvariable=self.var_atten_roll, font =("times new roman",12))
        Roll_entry.grid(row=0,column=3,pady=8)
        
        #Name
        Name_lbl = Label(Left_inside_frame, text="Name:", font =("times new roman",12,"bold"),bg ="white")
        Name_lbl.grid(row=1,column=0,padx=4, pady=8)
        
        Name_entry = ttk.Entry(Left_inside_frame, width=20,textvariable=self.var_atten_name,font =("times new roman",12))
        Name_entry.grid(row=1,column=1,pady=8)
        
        #Dep
        Dep_lbl = Label(Left_inside_frame, text="Department:", font =("times new roman",12,"bold"),bg ="white")
        Dep_lbl.grid(row=1,column=2)
        
        Dep_entry = ttk.Entry(Left_inside_frame, width=20, textvariable=self.var_atten_dep, font =("times new roman",12))
        Dep_entry.grid(row=1,column=3,pady=8)
        
        #time
        time_lbl = Label(Left_inside_frame, text="Time:",font =("times new roman",12,"bold"),bg ="white")
        time_lbl.grid(row=2,column=0)
        
        time_entry = ttk.Entry(Left_inside_frame, width=20, textvariable=self.var_atten_time, font =("times new roman",12))
        time_entry.grid(row=2,column=1,pady=8)
        
        #date
        date_lbl = Label(Left_inside_frame, text="Date:", font =("times new roman",12,"bold"),bg ="white")
        date_lbl.grid(row=2,column=2)
        
        date_entry = ttk.Entry(Left_inside_frame, width=20,textvariable=self.var_atten_date ,font =("times new roman",12))
        date_entry.grid(row=2,column=3,pady=8)
        
        #attendance
        attendance_lbl = Label(Left_inside_frame, text="Attendance Status:", font =("times new roman",12,"bold"),bg ="white")
        attendance_lbl.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(Left_inside_frame, textvariable=self.var_atten_attendance,font =("times new roman",12,"bold"),state="readonly",width=18)
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
       
        
        #bbuton frame
        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=600,height=37) 
        
        import_btn = Button(btn_frame,text = "Import csv",command=self.importCsv,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        import_btn.grid(row=0,column=0)
        
        export_btn = Button(btn_frame,text = "Export csv",command=self.exportCsv,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        update_btn = Button(btn_frame,text = "Update",width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        update_btn.grid(row=0,column=2)
        
        Reset_btn = Button(btn_frame,text = "Reset",command=self.reset_data,width=14, font=("times new romen",12,"bold"),bg = "blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
    
        
        # Right side level frame-------
        right_frame = LabelFrame(main_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Attendance Details", font=("times new romen",15,"bold"))
        right_frame.place(x=636,y=5,width=585,height=495)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=565,height=400) 
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)
        
        
    def back(self):
        self.root.destroy()
        
    ########## Fetch data ##########
    
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    # Import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File" , "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    
    # export csv
    def exportCsv(self):
        try:
            if(len(mydata)<1):
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfile(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*.csv"),("ALL File" , "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported",f"Your Data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

        #  !!!!!!!1 Export csv button not working  
        
    def getcursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        print(rows)
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        

if __name__ == "__main__":                                          
    root=Tk()
    obj=Attendance(root)
    root.mainloop()