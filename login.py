from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import time
import datetime 
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
    
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

        ###   variables ###
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pswd=StringVar()
        self.var_confpass=StringVar()

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
        imgbg = Image.open(r"Attendance_system\images\planebg.jpg")
        imgbg = imgbg.resize((1278,650), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=100,width=1278,height=650)
        
        #title
        title_lbl = Label(bg_img, text = "AUTOMATED FACE ATTENDANCE SYSTEM", font=("times new roman",25,"bold"),bg ="white", fg = "black")
        title_lbl.place(x=0,y=0, width = 1278, height=37)
        
        frame = Frame(self.root,bg="white")
        frame.place(x=490,y=200,width=340,height=400)
        
        img1 = Image.open(r"Attendance_system\images\download.png")
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="white",borderwidth=0)
        lblimg1.place(x=610,y=200,width=100,height=100)
        
        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
        
        #username
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)
        
        self.txtuser=StringVar()
        self.txtpass=StringVar()
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        # password
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=220)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=255,width=270)
        
        #icon image
        img2 = Image.open(r"Attendance_system\images\download.png")
        img2 = img2.resize((25,25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="white",borderwidth=0)
        lblimg2.place(x=535,y=352,width=25,height=25)
        
        #icon image 2
        img3 = Image.open(r"Attendance_system\images\download (1).jpeg")
        img3 = img3.resize((25,25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="white",borderwidth=0)
        lblimg3.place(x=535,y=420,width=25,height=25)
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd = 3, relief=RIDGE,fg ="white", bg="dodgerblue3",activeforeground="blue",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35) 
        
        #register button
        registerbtn=Button(frame,command=self.register_window,text="Sign Up",font=("times new roman",10,"bold"),bd = 3, borderwidth=0,fg ="blue", bg="white",activeforeground="white",activebackground="blue")
        registerbtn.place(x=0,y=350,width=120)
        
        #forgot password button
        registerbtn=Button(frame,command=self.forget_password_window, text="Forget Password",font=("times new roman",10,"bold"),bd = 3, borderwidth=0,fg ="blue", bg="white",activeforeground="white",activebackground="blue")
        registerbtn.place(x=15,y=370,width=120)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
    def login(self):
        if self.txtuser.get()==""  or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="shamina" and self.txtpass.get()=="sham":
            messagebox.showinfo("success","Welcome to Face Recognition attendance system project")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                            ))
            
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
        
    #########  Reset password function ###################
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","All fields are Required",parent= self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
                my_cursor = conn.cursor()
                query=("Select * from register where email=%s and securityQ=%s and securityA=%s ")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the correct security question")
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    #row2
                    my_cursor.execute(query,value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your Password has been reset, Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()
            
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To : {str(es)}",parent=self.root2)
    
    
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
            my_cursor = conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("My Error","Please Enter the Valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2,text="Forget Password", font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions", font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"))
                self.combo_security_Q["values"]=("Select", "Your Birth Place","Your first School","Your Pet name" )
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,textvariable=self.var_securityA, font=("times new roman", 15, "bold")) 
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password", font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman", 15, "bold")) 
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 20, "bold"),fg="white",bg="green")
                btn.place(x=120,y=300,width=100)
        
    
        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0")
        
        
        ###   variables ###
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pswd=StringVar()
        self.var_confpass=StringVar()
       

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
        imgbg = imgbg.resize((1277,650), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=100,width=1277,height=650)
        
        #title
        title_lbl = Label(bg_img, text = "REGISTRATION", font=("times new roman",25,"bold"),bg ="white", fg = "dark green")
        title_lbl.place(x=0,y=0, width = 1277, height=37)
        
        img3 = Image.open(r"Attendance_system\images\360_F_460710131_YkD6NsivdyYsHupNvO3Y8MPEwxTAhORh.jpg")
        img3 = img3.resize((500,700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=190,width=500,height=450)
        
        frame = Frame(self.root,bg="white")
        frame.place(x=490,y=190,width=740,height=450)
        
        register_lbl = Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),bg ="white",fg="green")
        register_lbl.place(x=20,y=20)

        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white") 
        fname.place(x=50,y=80)

        self.txt_fname=ttk.Entry(frame, textvariable=self.var_fname,font=("times new roman", 15)) 
        self.txt_fname.place(x=50,y=110,width=250)

        lname=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        lname.place(x=370,y=80)

        self.txt_lname=ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=110, width=250)

        #row2
        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black")
        contact.place(x=50,y=150)

        self.txt_contact=ttk.Entry(frame, textvariable=self.var_contact,font=("times new roman", 15)) 
        self.txt_contact.place(x=50,y=180,width=250)

        email=Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        email.place(x=370,y=150)

        self.txt_email=ttk.Entry(frame, textvariable=self.var_email,font=("times new roman",15)) 
        self.txt_email.place(x=370,y=180,width=250)
                
        security_Q = Label(frame,text="Select Sceurity Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50,y=220)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your first School","Your Pet Name")
        self.combo_security_Q.place(x=50,y=250,width=250)
        self.combo_security_Q.current(0)
                
        security_A = Label(frame,text="Select Answers", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370,y=220)        

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman",15)) 
        self.txt_security.place(x=370,y=250,width=250)
        
        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        pswd.place(x=50,y=290)

        self.txt_pswd=ttk.Entry(frame, textvariable=self.var_pswd,font=("times new roman",15)) 
        self.txt_pswd.place(x=50,y=320,width=250)
        
        confirm_pswd=Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        confirm_pswd.place(x=370,y=290)

        self.txt_confirm_pswd=ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman",15)) 
        self.txt_confirm_pswd.place(x=370,y=320,width=250)
        
        # checkbox button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check ,text="I Agree the Terms & Conditions", font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=350)
        
        # Register buttons
        img4=Image.open(r"Attendance_system\images\360_F_27899249_jpua6yZuHPLtcurgFzp77TFOEPuyPkUy.jpg")
        img4=img4.resize((200,45),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1 = Button(frame,image=self.photoimage4,borderwidth=0,cursor="hand2",command=self.register_data)
        b1.place(x=50,y=390,width=200)
        
        # login buttons
        img5=Image.open(r"Attendance_system\images\images (1).jpeg")
        img5=img5.resize((200,45),Image.ANTIALIAS)
        
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2 = Button(frame,image=self.photoimage5,borderwidth=0,cursor="hand2",command=self.return_login)
        b2.place(x=370,y=390,width=200)


    ###   Function declaration 
    def register_data(self):
        if self.var_fname.get()=="" or  self.var_email.get()=="" or  self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pswd.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password don't match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error",'Please agree our terms and Conditions')
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@31",database="attendancesystem")
            my_cursor = conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pswd.get()
                                                                                        
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
            
            
    def return_login(self):
        self.root.destroy()
            


if __name__ == "__main__":
    main()