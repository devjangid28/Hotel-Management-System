from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from details import Detailsroom


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root): 
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_security_A=StringVar()
    
        
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\24.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\28.jpeg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #icon images
         #2 img
        img2=Image.open(r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\27.jpeg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\26.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=397,width=25,height=25)
        
        #loginbutton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
         
        #registerbuttom
        registerbtn=Button(frame,text="Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forgetpassword
        forgotbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="Dev" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome Back",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_password.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access Only admin")
                if open_main:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
                    conn.commit()
                    conn.close()
                    
        #reset password
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security question",parent=self.root)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Please enter the correct answer",parent=self.root)
            else:
                query1 = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query1, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been updated successfully",parent=self.root)
                self.root2.destroy()
                
                

            
            
            
            #forgot password 
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your email to reset the password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            print(row)

            if row is None:
                messagebox.showerror("Error", "Please enter a valid username",parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

            l = Label(self.root2, text="Forget Password", font=("times new roman", 15, "bold"), fg="red", bg="white")
            l.place(x=0, y=10, relwidth=1)

            security_Q = Label(self.root2, text="Security Question", font=("times new roman",15, "bold"), bg="white")
            security_Q.place(x=50, y=80)

            self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
            self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Car Name")
            self.combo_security_Q.place(x=50, y=110, width=250)
            self.combo_security_Q.current(0)
            

            security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
            security_A.place(x=50, y=150)

            self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
            self.txt_security.place(x=50,y=180,width=250)
            
            new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
            new_password.place(x=50, y=220)

            self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
            self.txt_newpass.place(x=50,y=250,width=250)
            
            btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
            btn.place(x=100,y=290)
            
    

class Register:
    def __init__(self, root): 
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        
        
        #img1(background)
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\24.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\14.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=20,y=20)
        
        #label and entry
        fname=Label(frame,text="Frist Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        #row1
        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Brith Place","Your Pet Name","Your Car Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)
        
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_password.place(x=370,y=310)
        
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15))
        self.txt_confirm_password.place(x=370,y=340,width=250)
        
        #checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agreee The Terms and Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons
        img=Image.open(r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\17.jpeg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)
        
        img1=Image.open(r"C:\Users\asus_\OneDrive\Desktop\Hotel managemet System\18.jpeg")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)
        
   
        
        #function deceleraation
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password does not match with confirm password",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security_Q.get(),
                                                                                        self.var_security_A.get(),
                                                                                        self.var_password.get(),
                                                                                                  
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register Sucessfully",parent=self.root)
                
    def return_login(self):
        self.root.destroy()
    
                
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # 1 img
        img1 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/14.jpg")
        img1 = img1.resize((1550, 160), Image.BILINEAR)  # Changed from Image.ANTIALIAS to Image.BILINEAR
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=160)
        
        #logo
        img2 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/5.jpg")
        img2 = img2.resize((230, 160), Image.BILINEAR)  # Changed from Image.ANTIALIAS to Image.BILINEAR
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=160)
        
        #title
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        
        #MAIN FRMAE
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        
        #menu
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        #btn Frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        cust_btn.grid(row=0,column=0)
        
        room_btn=Button(btn_frame,text="ROOM",width=22,command=self.Roombooking,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",width=22,command=self.Detailsroom,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",width=22,command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        logout_btn.grid(row=4,column=0,pady=1)
        
        
        #right side img
        img3 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/2.jpg")
        img3 = img3.resize((1310, 590), Image.BILINEAR)  # Changed from Image.ANTIALIAS to Image.BILINEAR
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)
        
        
        #down img
        img4 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/15.jpg")
        img4 = img4.resize((230, 210), Image.BILINEAR)  # Changed from Image.ANTIALIAS to Image.BILINEAR
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=180)
        
        
        img5 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/16.jpg")
        img5 = img5.resize((230, 195), Image.BILINEAR)  # Changed from Image.ANTIALIAS to Image.BILINEAR
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=-3, y=410, width=230, height=190)
        
        
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
        
        
    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def Detailsroom(self):
        self.new_window=Toplevel(self.root)
        self.app=Detailsroom(self.new_window)
        
    def logout(self):
        self.root.destroy()
        
            
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()