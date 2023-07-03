from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
# -------------------First Image-----------------------------------------
        img1=Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/hotel1.png")
        img1=img1.resize((1550,110))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=110)

# -------------------------Logo-------------------------------------------------

        img2 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/logohotel.png")
        img2 = img2.resize((180, 110))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=180, height=110)

# -----------------------------------Title------------------------------------------------

        lbl_title=Label(self.root,text="HOTEL MANAGMENT SYSTEM",font=("times new roman",30),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=110,width=1550,height=45)

# -----------------------------------Main frame-------------------------------------------------

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=155,width=1550,height=620)

        # ----------------Menu------------------------
        lbl_menu = Label(main_frame,text="MENU", font=("times new roman", 15, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=180)

# -----------------------------------btn frame-------------------------------------------------

        btn_frame=Frame(main_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=178,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,justify='left',width=22,font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS",command=self.details_room, width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0,pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0,pady=1)

# ------------------------------Right side Image----------------------------

        img3 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/slide3.jpg")
        img3 = img3.resize((1360, 590))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=180, y=-5, width=1310, height=590)

# ----------------------Down Images----------------------------

        img4 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/myh.jpg")
        img4 = img4.resize((180, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=220, width=180, height=210)

        img5 = Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/khana.jpg")
        img5 = img5.resize((180, 190))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420,width=180, height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)


    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()