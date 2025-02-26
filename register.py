from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


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
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password does not match with confirm password")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition")
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
                messagebox.showinfo("Sucess","Register Sucessfully")
                
    def return_login(self):
        self.root.destroy()
    
            
        
        

        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
    
