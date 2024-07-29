from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Detailsroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        # Title
        lbl_title = Label(self.root, text=" ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open(r"C:/Users/asus_/OneDrive/Desktop/Hotel managemet System/5.jpg")
        img2 = img2.resize((100, 50), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=90, height=50)

        # Label frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 12, "bold"), padx=2)
        lableframeleft.place(x=5, y=50, width=540, height=350)
        
        lbl_floor = Label(lableframeleft, text="Floor", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        
        self.var_floor = StringVar()
        entry_floor = ttk.Entry(lableframeleft, width=20, textvariable=self.var_floor, font=("times new roman", 12, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)
        
        lbl_room = Label(lableframeleft, text="Room", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room.grid(row=1, column=0, sticky=W)
        
        self.var_room = StringVar()
        entry_room = ttk.Entry(lableframeleft, width=20, textvariable=self.var_room, font=("times new roman", 12, "bold"))
        entry_room.grid(row=1, column=1, sticky=W)
           
        lbl_roomtype = Label(lableframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)
        
        self.var_roomtype = StringVar()
        entry_roomtype = ttk.Entry(lableframeleft, width=20, textvariable=self.var_roomtype, font=("times new roman", 12, "bold"))
        entry_roomtype.grid(row=2, column=1, sticky=W)
        
        # Button
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
        # Table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)
        
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_Table = ttk.Treeview(Table_Frame, column=("floor", "roomno", "roomtype"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("floor", text="Floor")
        self.room_Table.heading("roomno", text="Room NO")
        self.room_Table.heading("roomtype", text="Room Type")
    
        self.room_Table["show"] = "headings"

        self.room_Table.column("floor", width=100)
        self.room_Table.column("roomno", width=100)
        self.room_Table.column("roomtype", width=100)
       
        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_floor.get() == "" or self.var_room.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All the fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details VALUES (%s, %s, %s)", (
                    self.var_floor.get(),
                    self.var_room.get(),
                    self.var_roomtype.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning", f"Some things went wrong: {str(es)}", parent=self.root)
                 
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
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
        
        self.var_floor.set(row[0]),
        self.var_room.set(row[1]),
        self.var_roomtype.set(row[2])
        
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter the mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="devjangid@28", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE details SET floor=%s,roomtype=%s WHERE roomno=%s",
                    (
                        self.var_floor.get(), self.var_roomtype.get(), self.var_room.get()
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
            query = "DELETE FROM details WHERE roomno=%s"
            value = (self.var_room.get(),)
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
        self.var_floor.set("")
        self.var_room.set("")
        self.var_roomtype.set("")
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Detailsroom(root)
    root.mainloop()
