from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1180x500+180+185")

        # ------------------------Variable-------------------------

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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",padx=2,font=("arial", 12,"bold"))
        labelframeleft.place(x=5,y=40,width=425,height=490)

# -------------------------------Label and Entry-----------------------------------
#cust_contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=18,font=("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        # ----------------------Fetch Data Button---------------------------
        btnFetchData = Button(labelframeleft,command=self.Fetch_contact, text="Fetch",font=("arial", 10, "bold"), bg="black", fg="gold",
                        width=9)
        btnFetchData.place(x=330,y=4)
#Check in Date:
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",12,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

#Check out Date:
        lbl_Check_out=Label(labelframeleft,text="Check_Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)

        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",12,"bold"))
        txt_Check_out.grid(row=2 ,column=1)

#Room Type

        label_RoomType=Label(labelframeleft,text="Room Type:",padx=2,pady=6,font=("arial", 12,"bold"))
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=27,state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

#Available Room:
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",12,"bold"))
        # txtRoomAvailable.grid(row=4 ,column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"),
                                      width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

#Meal:
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",12,"bold"))
        txtMeal.grid(row=5 ,column=1)

#No of Days:
        lblNoOfDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",12,"bold"))
        txtNoOfDays.grid(row=6 ,column=1)

#Paid Tax:
        lblNoOfDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",12,"bold"))
        txtNoOfDays.grid(row=7 ,column=1)

#Sub Total:
        lblNoOfDays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",12,"bold"))
        txtNoOfDays.grid(row=8 ,column=1)

# Total Cost:
        lblIdNumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",12,"bold"))
        txtIdNumber.grid(row=9 ,column=1)

# ---------------------Bill Button---------------------------------------

        btnBill = Button(labelframeleft, text="Bill",command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

# ----------------------------Buttons-----------------------------

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # -----------------------Right Side Image----------------------------------

        img3 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/bed.jpg")
        img3 = img3.resize((450, 300))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=730, y=50, width=450, height=250)

        # --------------------Table Frame Search System-----------------------------------

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", padx=2,
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=435, y=280, width=745, height=250)

        lblSearchBy = Label(Table_Frame, text="Search By:", bg="red", fg="White", font=("arial", 12, "bold"))
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=20,
                                    state="readonly")
        combo_Search["value"] = ("Search Option", "Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        textSerach = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=25, font=("arial", 13, "bold"))
        textSerach.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("arial", 10, "bold"), bg="black",
                           fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 10, "bold"),
                            bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=2)

        # ----------------------------------------Show data table---------------------------------------------

        details_Table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_Table.place(x=0, y=40, width=745, height=165)

        scroll_x = ttk.Scrollbar(details_Table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_Table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_Table, column=(
        "contact", "checkin", "checkout", "roomtype", "Room", "meal", "noOfdays"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkin", text="Check-in")
        self.room_Table.heading("checkout", text="Check-out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("Room", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noOfdays", text="NoOfDays")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkin", width=100)
        self.room_Table.column("checkout", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("Room", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noOfdays", width=100)
        self.room_Table.pack(fill=BOTH, expand=1)

        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#Add Data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aadil7611@",database="management")
                my_cursor=conn.cursor()
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

                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


# Get Cursor

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

#Update Data
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",
                              (

                                  self.var_checkin.get(),
                                  self.var_checkout.get(),
                                  self.var_roomtype.get(),
                                  self.var_roomavailable.get(),
                                  self.var_meal.get(),
                                  self.var_noofdays.get(),
                                  self.var_contact.get()
                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Room detail has been update successfully",parent=self.root)


#Delete Function


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                           database="management")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#Reset Function


    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        # ------------------------Fetch DAta----------------------------

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
                conn.commit()
            conn.close()


# ---------------All Data Fetch-----------------------------

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                           database="management")
            my_cursor = conn.cursor()
            query=("select Name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=430,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"),fg="blue")
                lbl.place(x=90,y=0)
#Gender
                conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                               database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"), fg="blue")
                lbl2.place(x=90, y=30)

#Email
                conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                               database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"), fg="blue")
                lbl3.place(x=90, y=60)

#Nationality
                conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                               database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lblNationality = Label(showDataframe, text=row, font=("arial", 12, "bold"), fg="blue")
                lblNationality.place(x=90, y=90)

#Address

                conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                               database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl1 = Label(showDataframe, text=row, font=("arial", 12, "bold"), fg="blue")
                lbl1.place(x=90, y=120)

                # ---------------------------------Search System--------------------------

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aadil7611@",
                                       database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Duplex"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * .1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == '__main__':
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()