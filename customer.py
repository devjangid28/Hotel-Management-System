from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # Title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/5.jpg")
        img2 = img2.resize((100, 50), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=90, height=50)

        # Label frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        lableframeleft.place(x=5, y=50, width=425, height=490)

        # Label and entry

        # Customer reference
        lbl_cust_ref = Label(lableframeleft, text="Customer Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(lableframeleft, textvariable=self.var_ref, width=22, font=("times new roman", 12, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer name
        cname = Label(lableframeleft, font=("arial", 12, "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(lableframeleft, textvariable=self.var_cust_name, font=("arial", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # Mother name
        lblmnname = Label(lableframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmnname.grid(row=2, column=0, sticky=W)

        txtmnname = ttk.Entry(lableframeleft, textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        txtmnname.grid(row=2, column=1)

        # Gender combobox
        lable_gender = Label(lableframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        lable_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(lableframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        lblPostCode = Label(lableframeleft, font=("arial", 12, "bold"), text="Post code:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(lableframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # Mobile number
        lblMobile = Label(lableframeleft, font=("arial", 12, "bold"), text="Mobile Number:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(lableframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(lableframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(lableframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(lableframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(lableframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("India", "Canada", "others")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # ID proof type combobox
        lblIdProof = Label(lableframeleft, font=("arial", 12, "bold"), text="ID Proof:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(lableframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("Aadhar Card", "Driving Licence", "others")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # ID number
        lblIdNumber = Label(lableframeleft, font=("arial", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(lableframeleft, textvariable=self.var_id_number, font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(lableframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(lableframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var1=StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var1, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
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
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("Ref", "Name", "Mother", "Gender", "PostCode", "Mobile", "Email", "Nationality", "IdProof", "IdNumber", "Address"),
                                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Refer No")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Mother", text="Mother Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("PostCode", text="PostCode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("IdProof", text="Id Proof")
        self.Cust_Details_Table.heading("IdNumber", text="Id Number")
        self.Cust_Details_Table.heading("Address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("Ref", width=100)
        self.Cust_Details_Table.column("Name", width=100)
        self.Cust_Details_Table.column("Mother", width=100)
        self.Cust_Details_Table.column("Gender", width=100)
        self.Cust_Details_Table.column("PostCode", width=100)
        self.Cust_Details_Table.column("Mobile", width=100)
        self.Cust_Details_Table.column("Email", width=100)
        self.Cust_Details_Table.column("Nationality", width=100)
        self.Cust_Details_Table.column("IdProof", width=100)
        self.Cust_Details_Table.column("IdNumber", width=100)
        self.Cust_Details_Table.column("Address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer (Ref, Name, Mother, Gender, Post, Mobile, Email, Nationality, IdProof, IdNumber, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                  (self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter the mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE customer SET Name=%s, Mother=%s, Gender=%s, Post=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s WHERE Ref=%s",
                                  (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(), self.var_ref.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Customer has been updated succesfully")

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
            my_cursor = conn.cursor()
            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.var_ref.get(),)
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
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
            
            
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        
        my_cursor.execute("select * from customer where " + str(self.search_var1.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()
     
            
            
            

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
