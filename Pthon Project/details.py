from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1180x500+180+185")

# ----------------------------Title-------------------------------------
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 15), bg="black", fg="gold",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1180, height=40)



# -------------------------Logo-------------------------------------------------

        img2 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/logohotel.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=30)

# ----------------------------Lable Frmae----------------------------------

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("arial", 12,"bold"))
        labelframeleft.place(x=5,y=40,width=500,height=350)

#Floor
        lbl_floor=Label(labelframeleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=18,font=("arial",12,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)


#Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=18,font=("arial",12,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)


#Room Type
        lbl_floor=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=18,font=("arial",12,"bold"))
        entry_floor.grid(row=2,column=1,sticky=W)

# ----------------------------Buttons-----------------------------

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # --------------------Table Frame Search System-----------------------------------

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", padx=2,
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=570, y=50, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_Table = ttk.Treeview(Table_Frame, column=(
            "floor", "roomno", "roomtype"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("floor", text="Floor")
        self.room_Table.heading("roomno", text="Room No")
        self.room_Table.heading("roomtype", text="Room Type")

        self.room_Table["show"] = "headings"

        self.room_Table.column("floor", width=100)
        self.room_Table.column("roomno", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.pack(fill=BOTH, expand=1)

        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                                   database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_RoomType.get(),

                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

        # ------------------------Fetch DAta----------------------------

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
                conn.commit()
            conn.close()

# Get Cursor

    def get_cursor(self, event=""):
            cursor_row = self.room_Table.focus()
            content = self.room_Table.item(cursor_row)
            row = content["values"]

            self.var_floor.set(row[0])
            self.var_roomNo.set(row[1])
            self.var_RoomType.set(row[2])

#Update Data
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",
                              (

                                  self.var_floor.get(),
                                  self.var_RoomType.get(),
                                  self.var_roomNo.get()

                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","New Room details has been updated Successfully",parent=self.root)

#Delete Function


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                           database="management")
            my_cursor = conn.cursor()
            query="delete from details where roomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#Reset Function


    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")



if __name__ == '__main__':
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()