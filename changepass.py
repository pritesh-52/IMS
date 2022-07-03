from tkinter import *
from tkinter import  messagebox ,filedialog
from PIL import Image, ImageTk
import mysql.connector as mysql
from tkinter import ttk
import os


class passchangeclass:

    def __init__(self,root):
            self.root = root
            self.root.geometry("500x300")
            self.root.config(bg="white")

            self.uname = Label(self.root, text="User_Name", bg="white", fg="black",
                               font=('goudy old style', '20', 'bold'))
            self.uname.place(x=25, y=60)

            self.username = StringVar()
            self.uname_entry = Entry(self.root, borderwidth=5, relief=SUNKEN, font=('TimesNewRoman', '20'),
                                     textvariable=self.username,
                                     bg="white", fg="black")
            self.uname_entry.place(x=200, y=65, width=260, height=35)

            self.passw = Label(self.root, text="Password", bg="white", fg="black",
                               font=('TimesNewRoman', '20', 'bold'))
            self.passw.place(x=25, y=120)

            self.password = StringVar()
            self.password_entry = Entry(self.root, borderwidth=5, relief=SUNKEN, font=('TimesNewRoman', '20'),
                                        textvariable=self.password, bg="white", fg="black", show='*')
            self.password_entry.place(x=200, y=130, width=260, height=35)

            login_ch = Button(self.root, text="Change", borderwidth=5, relief=RIDGE, fg="white", bg="#0b8e00",
                              font=('Open Sans', '24', 'bold'), command=self.pass_change)
            login_ch.place(width=160, height=45, x=160, y=190)
            login_ch.bind('<Return>', self.pass_change)
            login_ch.bind('<Button-1>', self.pass_change)

    def pass_change(self,event):
        uname = self.uname_entry.get()
        password = self.password_entry.get()
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("update admin set password='" + password + "' where username='" + uname + "'")
        cursor.execute("commit")
        self.uname_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        messagebox.showinfo("Update Status", "Updated SucessFully")
        con.close()

if __name__ == "__main__":
    root = Tk()
    obj = passchangeclass(root)
    root.mainloop()