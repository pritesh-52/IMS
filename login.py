from tkinter import *
from tkinter import  messagebox ,filedialog
from PIL import Image, ImageTk
import mysql.connector as mysql
from tkinter import ttk
import  os

import dashoard
import  changepass






class Example:
    def __init__(self, root):
        self.root=root
        self.root.title("Inventory Management System | Developed By Pritesh Bhatiya")
        self.root.state('zoomed')
        self.root.attributes('-alpha', 0.98)


        self.image = Image.open('images/lg.jpg')
        self.copy_of_image =  self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = ttk.Label(root, image=self.photo)
        self.label.bind('<Configure>',self.resize_image)
        self.label.pack(fill=BOTH, expand=YES)

        self.f1 = Frame(self.root, borderwidth=3, bg="white", relief=SOLID)
        self.f1.place(x=440, y=105, height=590, width=670)

        self.image_1 = Image.open("images/LOGO3.jpg")
        self.image_1 = self.image_1.resize((170, 170), Image.ANTIALIAS)
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        self.new = Label(self.f1, image=self.photo_1)
        self.new.place(x=240, y=40)

        self.uname = Label(self.f1, text="User_Name", bg="white", fg="black", font=('goudy old style', '24', 'bold'))
        self.uname.place(x=73, y=277)

        self.username = StringVar()
        self.uname_entry = Entry(self.f1, borderwidth=5, relief=SUNKEN, font=('TimesNewRoman', '20'), textvariable=self.username,
                            bg="white", fg="black")
        self.uname_entry.place(x=310, y=283, width=260, height=35)

        self.passw = Label(self.f1, text="Password", bg="white", fg="black", font=('TimesNewRoman', '24', 'bold'))
        self.passw.place(x=73, y=380)

        self.password = StringVar()
        self.password_entry = Entry(self.f1, borderwidth=5, relief=SUNKEN, font=('TimesNewRoman', '20'),
                               textvariable=self.password, bg="white", fg="black", show='*')
        self.password_entry.place(x=310, y=383, width=260, height=35)

        login_bt= Button(self.f1, text="Log-in", borderwidth=5, relief=RIDGE, fg="white", bg="#0b8e00",
                       font=('Open Sans', '28', 'bold'),command=self.login)
        login_bt.place(width=160, height=60, x=240, y=500)
        login_bt.bind('<Return>', self.login)
        #login_bt.bind("<Return>",lambda e: self.root.destroy())
        login_bt.bind('<Button-1>', self.login)

        link1 = Label(self.f1, text="Chage Password!", font=(12),fg="#041151",bg="white", cursor="hand2")
        link1.place(x=485,y=550)
        link1.bind("<Button-1>",self.cpass)


        global counter
        counter = 1
    def login(self,event):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("error", "All Fileds Are Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from registration where username=%s and password=%s", (self.username.get(), self.password.get()))
            self.uname_entry.delete(0,'end')
            self.password_entry.delete(0, 'end')
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalied User Name Or PassWord")
            else:
                self.root.destroy()
                os.system("python dashoard.py")

    def cpass(self,event):
            self.new_window = Toplevel(root)
            self.new_obj = changepass.passchangeclass(self.new_window)


    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image =  self.copy_of_image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label.config(image=self.photo)
        self.label.image = self.photo



if __name__=="__main__":

    root=Tk()
    obj = Example(root)
    root.mainloop()
