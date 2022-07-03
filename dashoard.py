# librarey import
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import *
from tkinter import messagebox
import webbrowser
from plyer import notification  # notification module import
import mysql.connector as mysql
import time
import os

import employee
import supplier
import product
import category
import sales
import reports
import login
import salespredict

from tkinter import messagebox, filedialog


class IMS:  # main class of the gui windows defined
    def __init__(self, root):  # constrtuort is used for create tkinter object
        self.root = root
        # self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="white")

        self.root.title("Inventory Management System | Developed By Pritesh Bhatiya")

        p1 = PhotoImage(file="logo.png")
        self.root.iconphoto(False, p1)

        notification.notify(
            title='Welcome To Inventory Management System',
            message='IMS',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico' bv.0

            timeout=2,  # seconds
        )

        # ===icon of the gui window ==#
        # self.icon = PhotoImage(file="images/logo1.png")

        # ===Title Of The Gui Window ==#
        title = Label(self.root, text="Inventory Management System With Sales Forecasting",
                      font=('times new roman', 32, 'bold'), bg="orange", fg="black", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)  # relwidth is used to set reltive width of the gui window
        # compound proptery is used to set  the image postion on the label proptery

        # ======Logout Button #===
        btn_logout = Button(self.root, text="Logout", font=('times new roman', 24, 'bold'), bg="#000099", fg="white",
                            cursor="hand2", command=self.login1)
        btn_logout.place(x=1350, y=10, height=50, width=150)
        btn_logout.bind('<Return>', self.login1)
        btn_logout.bind('<Button-1>', self.login1)

        # ==time date framw ==#
        '''self.header_frame = Frame(self.root, relief=SUNKEN, bd=2, bg="#052320")
        self.header_frame.place(x=0, y=70, relwidth=1,height=30)'''

        # ===clock set the onther part of the label gui ==#

        self.time = time.strftime("%I:%M")
        self.date = time.strftime("%d-%m-%y")

        self.clock_lbl = Label(self.root,
                               text=f'Welcome To Inventory Management System \t\t Date: {str(self.date)} \t\t Time: {str(self.time)}',
                               font=('times new roman', 18, 'bold'), bg="#052320", fg="white")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

        '''self.time=Label(self.root,text="Time: HH-MM-SS",font=('times new roman', 18, 'bold'), bg="#052320", fg="white")
        self.time.place(x=300,y=70,relwidth=1,height=30)'''

        # === create left menu === #

        self.logo = Image.open("images/menu_im.png")
        self.logo = self.logo.resize((200, 200), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        # left menu frame #
        leftmenu = Frame(self.root, relief=RIDGE, bd=2, bg="white")
        leftmenu.place(x=5, y=102, width=290, height=620)

        lbl_menulogo = Label(leftmenu, image=self.logo)
        lbl_menulogo.pack(side=TOP, fill=X)

        # ==create menu optio==#
        labll_menu = Label(leftmenu, text="Menu", font=('time new roman', 22, 'bold'), bg="#051f27", fg="white")
        labll_menu.pack(side=TOP, fill=X)
        # ==create button in menu section ==#

        self.right_arrow = PhotoImage(file="images/icons.png")

        btn_employee = Button(leftmenu, text="Employee", image=self.right_arrow, compound=LEFT, padx=15, anchor="w",
                              font=('times new roman', 20, 'bold'), bg="white", bd=3, command=self.employee1,
                              cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)
        btn_employee.bind('<Return>', self.employee1)
        btn_employee.bind('<Button-1>', self.employee1)

        btn_supplier = Button(leftmenu, text="Supplier", image=self.right_arrow, compound=LEFT, command=self.supplier1,
                              padx=15, anchor="w", font=('times new roman', 20, 'bold'), bg="white", bd=3,
                              cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)
        btn_supplier.bind('<Return>', self.supplier1)
        btn_supplier.bind('<Button-1>', self.supplier1)

        btn_category = Button(leftmenu, text="Category", image=self.right_arrow, compound=LEFT, command=self.category1,
                              padx=15, anchor="w",
                              font=('times new roman', 20, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        btn_category.bind('<Return>', self.category1)
        btn_category.bind('<Button-1>', self.category1)

        btn_product = Button(leftmenu, text="Product", image=self.right_arrow, compound=LEFT, command=self.product1,
                             padx=15, anchor="w",
                             font=('times new roman', 20, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        btn_product.bind('<Return>', self.product1)
        btn_product.bind('<Button-1>', self.product1)

        btn_sales = Button(leftmenu, text="Sales", image=self.right_arrow, compound=LEFT, command=self.sales1, padx=15,
                           anchor="w",
                           font=('times new roman', 20, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        btn_sales.bind('<Return>', self.sales1)
        btn_sales.bind('<Button-1>', self.sales1)

        btn_report = Button(leftmenu, text="Reports", image=self.right_arrow, compound=LEFT, padx=15, anchor="w",
                            font=('times new roman', 20, 'bold'), bg="white", bd=3, cursor="hand2",
                            command=self.report1)
        btn_report.pack(side=TOP, fill=X)

        btn_exit = Button(leftmenu, text="Exit", image=self.right_arrow, compound=LEFT, padx=15, anchor="w",
                          font=('times new roman', 20, 'bold'), bg="white", bd=3, cursor="hand2", command=quit)
        btn_exit.pack(side=TOP, fill=X)
        btn_report.bind('<Return>', self.report1)
        btn_report.bind('<Button-1>', self.report1)

        self.s1 = Frame(self.root, bg="#2E2E2E")
        self.s1.place(x=299, y=102, height=639, width=1020)

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from employee")
        emp = cursor.fetchall()
        self.lb_employee = Label(self.root, text=f'Total Employee \n[{str(len(emp))}]', bg="#180523", fg="white",
                                 font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7, cursor="hand2")
        self.lb_employee.place(x=320, y=110, height=190, width=300)

        cursor.execute("select *from supplier")
        sup = cursor.fetchall()
        self.lb_supplier = Label(self.root, text=f'Total Supplier \n[{str(len(sup))}]', bg="#006400", fg="white",
                                 font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_supplier.place(x=660, y=110, height=190, width=300)  # 006400

        cursor.execute("select *from category")
        cat = cursor.fetchall()
        self.lb_category = Label(self.root, text=f'Total Category  \n[{str(len(cat))}]', bg="#33060b", fg="white",
                                 font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_category.place(x=1000, y=110, height=190, width=300)  # 33060b

        self.rightmenu = Frame(self.root, relief=RIDGE, bd=2, bg="WHITE")
        self.rightmenu.place(x=1325, y=102, width=200, height=252)

        labll_right_menu = Label(self.rightmenu, text="Social Widget", font=('time new roman', 20, 'bold'),
                                 bg="#052320", fg="white")
        labll_right_menu.pack(side=TOP, fill=X)

        # google logo set#
        self.image1 = Image.open('images/google.png')
        self.image1 = self.image1.resize((60, 60), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        b1 = Button(root, text='Click Me !', image=self.photo1, cursor="hand2", relief=SOLID, borderwidth=4,
                    command=self.open_google)
        b1.place(x=1340, y=170)

        # gmail logo set #
        self.image2 = Image.open('images/logo-gmail-9953.png')
        self.image2 = self.image2.resize((60, 60), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        b2 = Button(root, text='Click Me !', image=self.photo2, cursor="hand2", relief=SOLID, borderwidth=4,
                    command=self.open_gmail)
        b2.place(x=1442, y=170)

        # linkdin logo #
        self.image3 = Image.open('images/linkedin-logo-png-1831.png')
        self.image3 = self.image3.resize((60, 60), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        b3 = Button(root, text='Click Me !', image=self.photo3, cursor="hand2", relief=SOLID, borderwidth=4,
                    command=self.open_linkdenn)
        b3.place(x=1340, y=270)

        # facebook logo
        self.image4 = Image.open('images/facebook.png')
        self.image4 = self.image4.resize((60, 60), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        b4 = Button(root, text='Click Me !', image=self.photo4, cursor="hand2", relief=SOLID, borderwidth=4,
                    command=self.open_facebook)
        b4.place(x=1442, y=270)

        cursor.execute("select *from product")
        pro = cursor.fetchall()
        self.lb_product = Label(self.root, text=f'Total Product \n[{str(len(pro))}]', bg="#d35400", fg="white",
                                font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_product.place(x=320, y=330, height=190, width=300)

        cursor.execute("select *from sales")
        sal = cursor.fetchall()
        self.lb_sales = Label(self.root, text=f'Total Sales \n[{str(len(sal))}]', bg="#021725", fg="white",
                              font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_sales.place(x=660, y=330, height=190, width=300)

        self.lb_pucrhase = Label(self.root, text="Total Reports\n[6]", bg="#800000", fg="white",
                                 font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_pucrhase.place(x=1000, y=330, height=190, width=300)  # 800000

        cursor.execute("SELECT SUM(amount)FROM sales")
        sal_val=IntVar()
        sal_val = cursor.fetchall()

        self.lb_sales_prediction = Label(self.root, text=f'Total Sales Value \n[59892389]', bg="#33060b", fg="white",
                                         font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_sales_prediction.place(x=320, y=550, height=190, width=300)

        self.lb_sales_prediction = Label(self.root, text="Total Stocks \n[150]", bg="#DC143C", fg="white",
                                         font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7)
        self.lb_sales_prediction.place(x=660, y=550, height=190, width=300)  # DC143C

        self.lb_sales_prediction = Label(self.root, text="Sales Prediction", bg="#180523", fg="white",
                                         font=('goudy old style', 24, 'bold'), relief=SOLID, bd=7, cursor="hand2")
        self.lb_sales_prediction.place(x=1000, y=550, height=190, width=300)
        # self.lb_sales_prediction.bind('<Return>', self.report1)
        self.lb_sales_prediction.bind('<Button-1>', self.sales_predition)

        # calnde add#
        cal = Calendar(root, selectmode="day", year=2021, month=12, day=20)
        cal.place(x=1325, y=380, width=200, height=230)

        ims = Label(root, text="IMS", font=('times new roman', 26, 'bold'), fg="black", bg="white")
        ims.place(x=1460, y=672)

        # red rectngle
        r1 = Frame(root, bg="red")
        r1.place(x=1425, y=720, height=15, width=15)

        r2 = Frame(root, bg="orange")
        r2.place(x=1455, y=720, height=15, width=15)

        r3 = Frame(root, bg="#32cd32")
        r3.place(x=1485, y=720, height=15, width=15)

        r4 = Frame(root, bg="#00008b")
        r4.place(x=1515, y=720, height=15, width=15)

        # ==footer part ==#
        lbl_footer = Label(self.root,
                           text="IMS Inventory Management System | Developed By Pritesh Bhatiya \n For Any Quires Contact Us 9033174261",
                           font=('times new roman', 14), bg="#052320", fg="white")
        lbl_footer.place(x=0, y=750, height=50, relwidth=1)

        global counter
        counter = 1

        global c1
        c1 = 1

        global c2
        c2 = 1

        global c3
        c3 = 1

        global c4
        c4 = 1

        global c5
        c5 = 1

        global c6
        c6 = 1

    def employee1(self, event):
        self.root.destroy()
        os.system("python employee.py")

    def supplier1(self, event):
        self.root.destroy()
        os.system("python supplier.py")

    def category1(self, event):
        self.root.destroy()
        os.system("python category.py")

    def product1(self, event):
        self.root.destroy()
        os.system("python product.py")

    def sales1(self, event):
        self.root.destroy()
        os.system("python sales.py")

    def report1(self, event):
        self.root.destroy()
        os.system("python reports.py")

    def login1(self, event):
        self.root.destroy()
        os.system("python login.py")

    def sales_predition(self, event):
        self.root.destroy()
        os.system("python salespredict.py")

    def open_google(self):
        webbrowser.open_new(r"https://www.google.com/")

    def open_gmail(self):
        webbrowser.open_new(r"https://mail.google.com/mail/u/1/")

    def open_linkdenn(self):
        webbrowser.open_new(r"https://www.linkedin.com/")

    def open_facebook(self):
        webbrowser.open_new(r"https://www.facebook.com/")


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)

    root.mainloop()

# using class method can be work it on to gui application