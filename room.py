from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import  datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        #variable
        
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # Title
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/5.jpg")
        img2 = img2.resize((100, 50), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=90, height=50)

        # Label frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("times new roman", 12, "bold"), padx=2)
        lableframeleft.place(x=5, y=50, width=425, height=490)

        lbl_cust_contat = Label(lableframeleft, text="Customer Contact", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contat.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(lableframeleft, textvariable=self.var_contact,width=20, font=("times new roman", 12, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btnFetchData = Button(lableframeleft, command=self.Fetch_contact,text="Fetch Data", font=("arial", 10, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=340, y=4)

        # Check in date
        check_in_date = Label(lableframeleft, font=("arial", 12, "bold"), text="Check In Date:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(lableframeleft, textvariable=self.var_checkin,font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check out date
        check_out_date = Label(lableframeleft, font=("arial", 12, "bold"), text="Check Out Date:", padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date = ttk.Entry(lableframeleft, textvariable=self.var_checkout,font=("arial", 13, "bold"), width=29)
        txtcheck_out_date.grid(row=2, column=1)

        # Room type
        lbl_RoomType = Label(lableframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT roomtype FROM details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(lableframeleft, textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available room
        lblRoomAvailable = Label(lableframeleft, font=("ariall", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        #txtRoomAvailable = ttk.Entry(lableframeleft, textvariable=self.var_roomavailable,font=("arial", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1)
        
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT roomno FROM details")
        rows = my_cursor.fetchall()
        
        combo_RoomNo = ttk.Combobox(lableframeleft, textvariable=self.var_roomavailable,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(lableframeleft, font=("ariall", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(lableframeleft, textvariable=self.var_meal,font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of days
        lblNoofDays = Label(lableframeleft, font=("ariall", 12, "bold"), text="No of Days:", padx=2, pady=6)
        lblNoofDays.grid(row=6, column=0, sticky=W)
        txtNoofDays = ttk.Entry(lableframeleft, textvariable=self.var_noofdays,font=("arial", 13, "bold"), width=29)
        txtNoofDays.grid(row=6, column=1)

        # Paid tax
        lblPaidTax = Label(lableframeleft, font=("ariall", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(lableframeleft, textvariable=self.var_paidtax,font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub total
        lblSubTotal = Label(lableframeleft, font=("ariall", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(lableframeleft, textvariable=self.var_actualtotal,font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total cost
        lblTotalCost = Label(lableframeleft, font=("ariall", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(lableframeleft, textvariable=self.var_total,font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # Bill button
        btnBill = Button(lableframeleft, text="Bill", command=self.total ,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Right side image
        img2 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/3.jpg")
        img2 = img2.resize((520, 200), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        # Table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var1 = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var1, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact", "Roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_table, column=("contact", "checkindate", "checkoutdate", "roomtype", "roomavailable", "meal", "noofdays"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkindate", text="Check In Date")
        self.room_Table.heading("checkoutdate", text="Check Out Date")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noofdays", text="No Of Days")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkindate", width=100)
        self.room_Table.column("checkoutdate", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("roomavailable", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noofdays", width=100)

        self.room_Table.pack(fill=BOTH, expand=1)

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query=("Select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This Number is not Correct",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=450,y=55,width=300,height=180)
            
            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=0)
            
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query=("Select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            
            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=30)
            
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query=("Select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            
            lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblEmail.place(x=0,y=60)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=60)
            
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query=("Select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            
            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=90)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=90)
            
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query=("Select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() 
            
            lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblAddress.place(x=0,y=120)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=120)
            
            self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
            self.fetch_data()
            
            
            
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All the fields are required",parent=self.root)
        else:
             try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.var_contact.get(),
                                                                                                     self.var_checkin.get(),
                                                                                                     self.var_checkout.get(),
                                                                                                     self.var_roomtype.get(),
                                                                                                     self.var_roomavailable.get(),
                                                                                                     self.var_meal.get(),
                                                                                                     self.var_noofdays.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked ",parent=self.root)
             except Exception as es:
                 messagebox.showerror("Warning",f"Some things went wrong:{str(es)}",parent=self.root)
                 
                 
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_row = self.room_Table.focus()
        content = self.room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        
        
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter the mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s WHERE Contact=%s",
                    (
                        self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), 
                        self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(),
                        self.var_contact.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
            finally:
                conn.close()

                
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete", "Customer has been deleted successfully", parent=self.root)
        else:
            if not mDelete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()
            
    
    def reset(self):   
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        
        
    def total(self):
        # Get the check-in and check-out dates from the respective variables
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        
        # Convert the date strings to datetime objects
        inDate = datetime.strptime(inDate, "%d/%m/%y")
        outDate = datetime.strptime(outDate, "%d/%m/%y")
        
        # Calculate the number of days between check-in and check-out
        self.var_noofdays.set(abs((outDate - inDate).days))
        
        if self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "luxury":
            q1 = 3000.0  # Cost for meal
            q2 = 7000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        if self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "luxury":
            q1 = 5000.0  # Cost for meal
            q2 = 9000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
            
            
        if self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "luxury":
            q1 = 10000.0  # Cost for meal
            q2 = 7000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        if self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Single":
            q1 = 6000.0  # Cost for meal
            q2 = 5000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        if self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single":
            q1 = 2000.0  # Cost for meal
            q2 = 5000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
            
            
        if self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single":
            q1 = 7000.0  # Cost for meal
            q2 = 9000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        
        if self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Double":
            q1 = 900.0  # Cost for meal
            q2 = 1000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        if self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double":
            q1 = 1300.0  # Cost for meal
            q2 = 1800.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
            
            
        if self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double":
            q1 = 3000.0  # Cost for meal
            q2 = 7000.0  # Cost for luxury room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total daily cost
            q5 = q3 * q4  # Total cost for all days

            tax_amount = q5 * 0.1  # 10% tax
            total_with_tax = q5 + tax_amount  # Total amount including tax

            Tax = "Rs. " + str("%.2f" % tax_amount)
            ST = "Rs. " + str("%.2f" % q5)
            TT = "Rs. " + str("%.2f" % total_with_tax)

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
            
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        
        try:
            search_column = str(self.search_var1.get())
            search_value = str(self.txt_search.get())

            # List of allowed columns to prevent SQL injection
            allowed_columns = ["Contact", "check_in", "check_out", "roomtype","Roomavailable","meal","noofdays"]  # Add your actual column names here

            if search_column not in allowed_columns:
                raise ValueError(f"Invalid column name: {search_column}")

            query = f"SELECT * FROM room WHERE {search_column} LIKE %s"
            values = (f"%{search_value}%",)

            my_cursor.execute(query, values)
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.room_Table.delete(*self.room_Table.get_children())
                for row in rows:
                    self.room_Table.insert("", END, values=row)
            
        except mysql.connector.Error as err:
            messagebox.showwarning("Warning", f"Something went wrong: {str(err)}", parent=self.root)
        except ValueError as ve:
            messagebox.showwarning("Warning", str(ve), parent=self.root)
        finally:
            conn.close()

        
                                                            


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
