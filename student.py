from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1273x650+0+0")
        self.root.title("Student Details")
        
        #variables========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        #first image
        img1 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\facial-recognition_0.jpg")
        img1 = img1.resize((800,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=100)

        #Third image
        img3 = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\1_Hmqbvj-Y5jCkz5-53o8G_g.jpg")
        img3 = img3.resize((500,150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=800,y=0,width=500,height=100)
        
        
        #bg image
        imgbg = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\planebg.jpg")
        imgbg = imgbg.resize((1273,650), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=100,width=1273,height=650)
        
        #title
        title_lbl = Label(bg_img, text = "STUDENTS DETAILS", font=("times new roman",20,"bold"),bg ="white", fg = "darkgreen")
        title_lbl.place(x=0,y=0, width = 1270, height=25)
        
        ## back button
        back_btn = Button(bg_img,text = "Back",  command=self.back,width=14,font=("times new romen",15,"bold"),bg = "red",fg="white")
        back_btn.place(x=1160,y=0,width=80,height=25)
        
        #frame
        main_frame = Frame(bg_img,bd=2,bg="white")#############
        main_frame.place(x=15,y=31,width=1230,height=500)
        
        
        #left side level frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Student Details", font=("times new romen",10,"bold"))
        Left_frame.place(x=10,y=2,width=620,height=495)
        
        img_left = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1349297974-612x612.jpg")
        img_left = img_left.resize((610,200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=611,height=125)
        
        
        #current course
        Current_Course_frame = LabelFrame(Left_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Current Course Information", font=("times new romen",10,"bold"))
        Current_Course_frame.place(x=4,y=122,width=611,height=95)
        
        #department 
        dep_lbl = Label(Current_Course_frame, text="Department", font =("times new roman",10,"bold"),bg ="white")
        dep_lbl.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dep,font =("times new roman",8,"bold"),state="readonly")
        dep_combo["values"] = ("Select Department","CSE","CSBS","AIML","IT","ECE","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #Course
        Course_lbl = Label(Current_Course_frame, text="Course", font =("times new roman",10,"bold"),bg ="white")
        Course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        Course_combo=ttk.Combobox(Current_Course_frame,textvariable= self.var_course,font =("times new roman",8,"bold"),state="readonly")
        Course_combo["values"] = ("Select Course","OS","COA","AI","IoT","OOPS","DSA","Automata","ML","DBMS","Cryptography")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_lbl = Label(Current_Course_frame, text="Year", font =("times new roman",10,"bold"),bg ="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font =("times new roman",8,"bold"),state="readonly")
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_lbl = Label(Current_Course_frame, text="Semester", font =("times new roman",10,"bold"),bg ="white")
        semester_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(Current_Course_frame,textvariable= self.var_semester,font =("times new roman",8,"bold"),state="readonly")
        semester_combo["values"] = ("Select Semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        Class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Class Student Information", font=("times new romen",10,"bold"))
        Class_student_frame.place(x=5,y=220,width=610,height=255)
        
        #student id
        studentId_lbl = Label(Class_student_frame, text="StudentID:", font =("times new roman",10,"bold"),bg ="white")
        studentId_lbl.grid(row=0,column=0,padx=10, pady=5,sticky=W)
        
        studentId_entry = ttk.Entry(Class_student_frame,textvariable=self.var_std_id, width=20,font =("times new roman",8))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentName_lbl = Label(Class_student_frame, text="Student Name:", font =("times new roman",10,"bold"),bg ="white")
        studentName_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry = ttk.Entry(Class_student_frame,textvariable=self.var_std_name, width=20,font =("times new roman",8))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        classDivision_lbl = Label(Class_student_frame, text="Class Division:", font =("times new roman",10,"bold"),bg ="white")
        classDivision_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font =("times new roman",8,"bold"),state="readonly",width=18)
        div_combo["values"] = ("Select division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #Roll No
        rollNo_lbl = Label(Class_student_frame, text="Roll No:", font =("times new roman",10,"bold"),bg ="white")
        rollNo_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        rollNo_entry = ttk.Entry(Class_student_frame,textvariable=self.var_roll, width=20,font =("times new roman",8))
        rollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_lbl = Label(Class_student_frame, text="Gender:", font =("times new roman",10,"bold"),bg ="white")
        gender_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font =("times new roman",8,"bold"),state="readonly",width=18)
        gender_combo["values"] = ("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #dob
        dob_lbl = Label(Class_student_frame, text="DOB:", font =("times new roman",10,"bold"),bg ="white")
        dob_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry = ttk.Entry(Class_student_frame, textvariable=self.var_dob, width=20,font =("times new roman",8))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        Email_lbl = Label(Class_student_frame, text="Email:", font =("times new roman",10,"bold"),bg ="white")
        Email_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Email_entry = ttk.Entry(Class_student_frame,textvariable=self.var_email, width=20,font =("times new roman",8))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone No
        PhoneNo_lbl = Label(Class_student_frame, text="Phone No:", font =("times new roman",10,"bold"),bg ="white")
        PhoneNo_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        PhoneNo_entry = ttk.Entry(Class_student_frame,textvariable=self.var_phone, width=20,font =("times new roman",8))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        Address_lbl = Label(Class_student_frame, text="Address:", font =("times new roman",10,"bold"),bg ="white")
        Address_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        Address_entry = ttk.Entry(Class_student_frame, textvariable=self.var_address,width=20,font =("times new roman",8))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher 
        Teacher_lbl = Label(Class_student_frame, text = "Teacher:", font =("times new roman",10,"bold"),bg ="white")
        Teacher_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        Teacher_entry = ttk.Entry(Class_student_frame, textvariable=self.var_teacher,width=20,font =("times new roman",8))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio = StringVar()
        radiobutton1 = ttk.Radiobutton(Class_student_frame,variable=self.var_radio, text = "Take Photo Sample", value="Yes")
        radiobutton1.grid(row=5,column=0)
        
        radiobutton2 = ttk.Radiobutton(Class_student_frame,variable=self.var_radio, text = "No Photo Sample", value="No")
        radiobutton2.grid(row=5,column=1)

        
        #bbuton frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=173,width=606,height=65) 
        
        save_btn = Button(btn_frame,text = "Save",command= self.add_data,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn = Button(btn_frame,text = "Update",command= self.update_data,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        Delete_btn = Button(btn_frame,text = "Delete",command= self.delete_data,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn = Button(btn_frame,text = "Reset",command= self.reset_data,width=14,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        
        # UpdatePhoto_btn.grid(row=1,column=1)
        btn_frame1 = Frame(Class_student_frame,bd = 2, relief=RIDGE,bg="white") 
        btn_frame1.place(x=0,y=205,width=605,height=60)
        
        TakePhoto_btn = Button(btn_frame1,text = "Take Photo Sample",command=self.generate_dataset,width=30,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        TakePhoto_btn.grid(row=0,column=0)
        
        UpdatePhoto_btn = Button(btn_frame1,text = "Update Photo Sample",command=self.generate_dataset,width=30,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        UpdatePhoto_btn.grid(row=0,column=1)
        
        
        #right side level frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Student Details", font=("times new romen",10,"bold"))
        right_frame.place(x=636,y=2,width=585,height=495)
        
        img_right = Image.open(r"C:\Shamina\projects\Flask_project\Attendance_system\images\istockphoto-1284671681-612x612.jpg")
        img_right = img_right.resize((611,300), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=611,height=150)
        
    
        #Search System---------
        search_frame = LabelFrame(right_frame,bd=2,bg="white",fg="dark green",relief=RIDGE,text="Search System", font=("times new romen",10,"bold"))
        search_frame.place(x=5,y=150,width=573,height=60)
        
        search_lbl = Label(search_frame,text="Search By:",font=("times new romen",10,"bold"),bg="red",fg="white")
        search_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font =("times new roman",8,"bold"),state="readonly")
        search_combo["values"] = ("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_frame, width=15,font =("times new roman",8))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        search_btn = Button(search_frame,text = "search",width=10,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        ShowAll_btn = Button(search_frame,text = "Show All",width=10,font=("times new romen",12,"bold"),bg = "blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)
        
        #table frame------
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=573,height=250)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","Id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width = 100)
        self.student_table.column("course",width = 100)
        self.student_table.column("year",width = 100)
        self.student_table.column("sem",width = 100)
        self.student_table.column("Id",width = 100)
        self.student_table.column("name",width = 100)
        self.student_table.column("div",width = 100)
        self.student_table.column("roll",width = 100)
        self.student_table.column("gender",width =100)
        self.student_table.column("dob",width = 100)
        self.student_table.column("email",width = 100)
        self.student_table.column("phone",width = 100)
        self.student_table.column("address",width = 100)
        self.student_table.column("teacher",width = 100)
        self.student_table.column("photo",width = 110)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def update_radio_status(self):
        self.var_radio.set(self.var_radio.get())
        
    #function ----
    
    def back(self):
        self.root.destroy()
        # #####    make function to go back 
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio.get()
                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details have been added Succesfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)

    #--------fetch data---------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data =my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        

    #-----get cursor---------
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 
        
        #print(data)
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14]),
        
    #-----update function------
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you Want to update this student Details", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll_no=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()                    
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




    #------ delete Function--------
    def delete_data(self):
        if self.var_std_id=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("student Delete Page","Do you Want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id = %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Suceessfully Deleted student Details",parent = self.root)
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
    #-----Reset----
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set(""),
    

    def search_data(self):
         pass


    #-----------Generate data set or Take photo Samples-------
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id =0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll_no=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        "Yes",
                        self.var_std_id.get()==id+1                   
                    ))
            
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #Load Predefined ---
                face_Classifier = cv2.CascadeClassifier("Attendance_system\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_Classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Attendance_system/data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complited!!!")
                #########  after generating datsets complited photo sample status should be yes in data base please make it######
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}", parent=self.root)
        


    
    
if __name__ == "__main__":                                          
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
