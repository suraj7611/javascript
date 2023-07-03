from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")

        self.bg=ImageTk.PhotoImage(file="C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/bgn.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg='black')
        frame.place(x=550,y=150,width=340,height=450)

        img1=Image.open("C:/Users/SURAJ PAL/OneDrive/Desktop/Pthon Project/images/LoginIconAppl.png")
        img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0,)
        lblimg1.place(x=610,y=155,width=100,height=100)





if __name__ == '__main__':
    root=Tk()
    app=Login_window(root)
    root.mainloop()