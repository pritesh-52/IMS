#librarey import
from tkinter import  *
from PIL import Image,ImageTk
from tkcalendar import  *
from tkinter import  ttk
import mysql.connector as mysql
from  tkinter import  messagebox
from  fpdf import FPDF
from tkinter import  messagebox ,filedialog
import  employee
import  supplier
import  product
import  category
import  sales
import  login
import os
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
import pandas


import pyodbc

class reportclass:    #main class of the gui windows defined
    def __init__(self,root):   #constrtuort is used for create tkinter object
        self.root=root
        #self.root.geometry("1100x500+220+130")
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()  # fouce evenet used to focus on the screen

        root.title("Inventory Management System | Developed By Pritesh Bhatiya")
        f1 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f1.place(x=5, y=10, width=450, height=400)


        dashbboard_button = Button(root, text="Dashboard", font=('goudy old style', 16, 'bold'), bg="#163332",
                                    fg="white",cursor="hand2",command=self.dashboard1)
        dashbboard_button.place(x=1410,y=10, width=120, height=35)

        l1 = Label(f1, text="Employee", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)

        pdf = Button(f1, text="Save As PDF", font=('goudy old style', 18, 'bold'), bg="#f30000", fg="white",
                                       cursor="hand2",command=self.first_pdf)
        pdf.place(x=260, y=50, width=150, height=35)


        data_show = Frame(f1, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=90, height=300,relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel = ttk.Treeview(data_show,
                                  columns=("Emp No", "Name", "Email", "Contact No", "Gender", "D.O.B", "D.O.J", "Salary", "Address", "Password",
        "User Type"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel.xview)
        scroll_y.config(command=self.tabel.yview)

        self.tabel.heading("Emp No", text="Emp No")
        self.tabel.heading("Name", text="Name")
        self.tabel.heading("Email", text="Email")
        self.tabel.heading("Contact No", text="Contact No")
        self.tabel.heading("Gender", text="Gender")
        self.tabel.heading("D.O.B", text="D.O.B")
        self.tabel.heading("D.O.J", text="D.O.J")
        self.tabel.heading("Salary", text="Salary")
        self.tabel.heading("Address", text="Address")
        self.tabel.heading("Password", text="Password")
        self.tabel.heading("User Type", text="User Type")
        self.tabel['show'] = 'headings'

        self.tabel.column("Emp No", width=100)
        self.tabel.column("Name", width=180)
        self.tabel.column("Email", width=180)
        self.tabel.column("Contact No", width=100)
        self.tabel.column("Gender", width=100)
        self.tabel.column("D.O.B", width=100)
        self.tabel.column("D.O.J", width=100)
        self.tabel.column("Salary", width=100)
        self.tabel.column("Address", width=200)
        self.tabel.column("Password", width=100)
        self.tabel.column("User Type", width=100)
        self.tabel.pack(fill=BOTH, expand=1)
        #self.tabel.bind("<ButtonRelease-1>")
        self.fetch()

#second part

        f2 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f2.place(x=480, y=10, width=450, height=400)

        l1 = Label(f2, text="Supplier", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)

        pdf = Button(f2, text="Save As PDF", font=('goudy old style', 18, 'bold'), bg="#f30000", fg="white",
                     cursor="hand2",command=self.second_pdf)
        pdf.place(x=260, y=50, width=150, height=35)

        data_show = Frame(f2, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=90, height=300, relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_1 = ttk.Treeview(data_show,
                                  columns=(
                                  "Invoice_No", "Supplier_Name", "GST_Number", "Contact_No", "Supply_Product", "Price", "qty","Other_Information"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_1.xview)
        scroll_y.config(command=self.tabel_1.yview)


        self.tabel_1.heading("Invoice_No", text="Invoice_No")
        self.tabel_1.heading("Supplier_Name", text="Supplier_Name")
        self.tabel_1.heading("GST_Number", text="GST_Number")
        self.tabel_1.heading("Contact_No", text="Contact_No")
        self.tabel_1.heading("Supply_Product", text="Supply_Product")
        self.tabel_1.heading("Price", text="Price")
        self.tabel_1.heading("qty", text="qty")
        self.tabel_1.heading("Other_Information", text="Other_Information")
        self.tabel_1['show'] = 'headings'

        self.tabel_1.column("Invoice_No", width=100)
        self.tabel_1.column("Supplier_Name", width=150)
        self.tabel_1.column("GST_Number", width=180)
        self.tabel_1.column("Contact_No", width=100)
        self.tabel_1.column("Supply_Product", width=150)
        self.tabel_1.column("Price", width=100)
        self.tabel_1.column("qty", width=50)
        self.tabel_1.column("Other_Information", width=220)
        self.tabel_1.pack(fill=BOTH, expand=1)
        self.fetch_1()

#third part

        f3 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f3.place(x=955, y=10, width=450, height=400)

        l1 = Label(f3, text="Category", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)

        pdf = Button(f3, text="Save As PDF", font=('goudy old style', 18, 'bold'), bg="#f30000", fg="white",
                     cursor="hand2",command=self.third_pdf)
        pdf.place(x=260, y=50, width=150, height=35)

        data_show = Frame(f3, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=90, height=300, relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_2 = ttk.Treeview(data_show,
                                    columns=(
                                        "C_id", "Category_Type", "Category_Name", "Category_Code"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_2.xview)
        scroll_y.config(command=self.tabel_2.yview)

        self.tabel_2.heading("C_id", text="C_id")
        self.tabel_2.heading("Category_Type", text="Category_Type")
        self.tabel_2.heading("Category_Name", text="Category_Name")
        self.tabel_2.heading("Category_Code", text="Category_Code")
        self.tabel_2['show'] = 'headings'

        self.tabel_2.column("C_id", width=50)
        self.tabel_2.column("Category_Type", width=180)
        self.tabel_2.column("Category_Name", width=200)
        self.tabel_2.column("Category_Code", width=100)
        self.tabel_2.pack(fill=BOTH, expand=1)
        self.fetch_2()

#fourth part

        f4 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f4.place(x=5, y=420, width=450, height=400)

        l1 = Label(f4, text="Product", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)

        pdf = Button(f4, text="Save As PDF", font=('goudy old style', 18, 'bold'), bg="#f30000", fg="white",
                     cursor="hand2",command=self.fourth_pdf)
        pdf.place(x=260, y=50, width=150, height=35)

        data_show = Frame(f4, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=90, height=280, relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_4 = ttk.Treeview(data_show,
                                    columns=(
                                        "P_id", "Category_Type", "Product_Name", "Price","QTY","Amount","Status"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_4.xview)
        scroll_y.config(command=self.tabel_4.yview)

        self.tabel_4.heading("P_id", text="P_id")
        self.tabel_4.heading("Category_Type", text="Category_Type")
        self.tabel_4.heading("Product_Name", text="Product_Name")
        self.tabel_4.heading("Price", text="Price")
        self.tabel_4.heading("QTY", text="QTY")
        self.tabel_4.heading("Amount", text="Amount")
        self.tabel_4.heading("Status", text="Status")
        self.tabel_4['show'] = 'headings'

        self.tabel_4.column("P_id", width=50)
        self.tabel_4.column("Category_Type", width=220)
        self.tabel_4.column("Product_Name", width=180)
        self.tabel_4.column("Price", width=100)
        self.tabel_4.column("QTY", width=50)
        self.tabel_4.column("Amount", width=100)
        self.tabel_4.column("Status", width=150)
        self.tabel_4.pack(fill=BOTH, expand=1)
        self.fetch_3()

#fifth part
        f5 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f5.place(x=480, y=420, width=450, height=400)

        l1 = Label(f5, text="Sales", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)

        pdf = Button(f5, text="Save As PDF", font=('goudy old style', 18, 'bold'), bg="#f30000", fg="white",
                     cursor="hand2",command=self.fifth_pdf)
        pdf.place(x=260, y=50, width=150, height=35)

        data_show = Frame(f5, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=90, height=280, relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_5= ttk.Treeview(data_show,
                                    columns=(
                                        "S_id", "Name", "Contact_No", "Product_Name","Price","QTY","Discout","GST_18%","GST_28%","Amount","Date"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_5.xview)
        scroll_y.config(command=self.tabel_5.yview)

        self.tabel_5.heading("S_id", text="S_id")
        self.tabel_5.heading("Name", text="Name")
        self.tabel_5.heading("Contact_No", text="Contact_No")
        self.tabel_5.heading("Product_Name", text="Product_Name")
        self.tabel_5.heading("Price", text="Price")
        self.tabel_5.heading("QTY", text="QTY")
        self.tabel_5.heading("Discout", text="Discout")
        self.tabel_5.heading("GST_18%", text="GST_18%")
        self.tabel_5.heading("GST_28%", text="GST_28%")
        self.tabel_5.heading("Amount", text="Amount"),
        self.tabel_5.heading("Date", text="Date")
        self.tabel_5['show'] = 'headings'

        self.tabel_5.column("S_id", width=70)
        self.tabel_5.column("Name", width=150)
        self.tabel_5.column("Contact_No", width=150)
        self.tabel_5.column("Product_Name", width=200)
        self.tabel_5.column("Price", width=70)
        self.tabel_5.column("QTY", width=100)
        self.tabel_5.column("Discout", width=100)
        self.tabel_5.column("GST_18%", width=100)
        self.tabel_5.column("GST_28%", width=100)
        self.tabel_5.column("Amount", width=100),
        self.tabel_5.column("Date", width=100),
        self.tabel_5.pack(fill=BOTH, expand=1)
        self.fetch_4()

        rightmenu = Frame(root, relief=RIDGE, bd=2, bg="white")
        rightmenu.place(x=1385, y=490, width=140, height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")
        btn_employee = Button(rightmenu, text="Employee", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, command=self.employee1,
                              cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)


        btn_supplier = Button(rightmenu, text="Supplier", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, command=self.supplier1,
                              cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = Button(rightmenu, text="Category", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, command=self.category1,
                              cursor="hand2")
        btn_category.pack(side=TOP, fill=X)


        btn_product = Button(rightmenu, text="Product", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                             font=('times new roman', 14, 'bold'), command=self.product1, bg="white", bd=3,
                             cursor="hand2")
        btn_product.pack(side=TOP, fill=X)

        btn_sales = Button(rightmenu, text="Sales", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                           font=('times new roman', 14, 'bold'), command=self.sales1, bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)


        btn_purchase = Button(rightmenu, text="Report", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.report1)
        btn_purchase.pack(side=TOP, fill=X)


        self.image3 = Image.open('images/import.jpg')
        self.image3 = self.image3.resize((400,300), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.new3 = Label(root, image=self.photo3, relief=SOLID, borderwidth=2)
        self.new3.place(x=950, y=450)

        word_lable = Label(root, text="W_orldwide S_upply", font=('Microsoft Sans Serif', 22, 'bold'), bg="white",
                           fg="black", bd=3)
        word_lable.place(x=1000, y=740)

        ims = Label(root, text="IMS", font=('times new roman', 26, 'bold'), fg="black", bg="white")
        ims.place(x=1460, y=740)

        # red rectngle
        r1 = Frame(root, bg="red")
        r1.place(x=1425, y=778, height=15, width=15)

        r2 = Frame(root, bg="orange")
        r2.place(x=1455, y=778, height=15, width=15)

        r3 = Frame(root, bg="#32cd32")
        r3.place(x=1485, y=778, height=15, width=15)

        r4 = Frame(root, bg="#00008b")
        r4.place(x=1515, y=778, height=15, width=15)

        self.root.bind("<Escape>", exit)



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
        c6=1

    def first_pdf(self):
        pagesize = (10 * inch, 10 * inch)
        pdf = SimpleDocTemplate(f"E:\IMS PROJECT\REPORTS\Employee_Data.pdf", pagesize=pagesize)
        flow_obj = []
        # table header

        td = [["Emp No", "Name", "Email", "Contact No", "Gender", "D.O.B", "D.O.J", "Salary", "Address", "Department",
               "User Type"]]

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        data_obj = con.cursor()
        data_obj.execute("select * from employee")
        data_row = data_obj.fetchall()
        for row in data_row:
            data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
            td.append(data)
        table = Table(td)

        ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black),
                         # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                         ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
                         ("LEFTPADDING", (0, 0), (-1, -1), 2),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                         ("BACKGROUND", (0, 1), (-1, -1), colors.white)])

        table.setStyle(ts)
        flow_obj.append(table)
        pdf.build(flow_obj)
        messagebox.showinfo('Notifications', 'PDF HAS BEEN SAVED')

    def second_pdf(self):
        pagesize = (10 * inch, 10 * inch)
        pdf = SimpleDocTemplate(f"E:\IMS PROJECT\REPORTS\Supplier_Data.pdf", pagesize=pagesize)
        flow_obj = []
        # table header

        td = [["Invoice_No", "Supplier_Name", "GST_Number", "Contact_No", "Supply_Product", "Price", "qty","Other_Information"]]

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        data_obj = con.cursor()
        data_obj.execute("select * from supplier")
        data_row = data_obj.fetchall()
        for row in data_row:
            data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            td.append(data)
        table = Table(td)

        ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black),
                         # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                         ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
                         ("LEFTPADDING", (0, 0), (-1, -1), 2),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                         ("BACKGROUND", (0, 1), (-1, -1), colors.white)])

        table.setStyle(ts)
        flow_obj.append(table)
        pdf.build(flow_obj)
        messagebox.showinfo('Notifications', 'PDF HAS BEEN SAVED')

    def third_pdf(self):
        pagesize = (10 * inch, 10 * inch)
        pdf = SimpleDocTemplate(f"E:\IMS PROJECT\REPORTS\Category_Data.pdf", pagesize=pagesize)
        flow_obj = []
        # table header

        td = [["C_id", "Category_Type", "Category_Name", "Category_Code"]]

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        data_obj = con.cursor()
        data_obj.execute("select * from category")
        data_row = data_obj.fetchall()
        for row in data_row:
            data = [row[0], row[1], row[2], row[3]]
            td.append(data)
        table = Table(td)

        ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black),
                         # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                         ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
                         ("LEFTPADDING", (0, 0), (-1, -1), 2),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                         ("BACKGROUND", (0, 1), (-1, -1), colors.white)])

        table.setStyle(ts)
        flow_obj.append(table)
        pdf.build(flow_obj)
        messagebox.showinfo('Notifications', 'PDF HAS BEEN SAVED')

    def fourth_pdf(self):
        pagesize = (10 * inch, 10 * inch)
        pdf = SimpleDocTemplate(f"E:\IMS PROJECT\REPORTS\Product_Data.pdf", pagesize=pagesize)
        flow_obj = []
        # table header

        td = [["P_id", "Category_Type", "Product_Name", "Price","QTY","Amount","Status"]]

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        data_obj = con.cursor()
        data_obj.execute("select * from product")
        data_row = data_obj.fetchall()
        for row in data_row:
            data = [row[0], row[1], row[2], row[3],row[4],row[5],row[6]]
            td.append(data)
        table = Table(td)

        ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black),
                         # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                         ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
                         ("LEFTPADDING", (0, 0), (-1, -1), 2),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                         ("BACKGROUND", (0, 1), (-1, -1), colors.white)])

        table.setStyle(ts)
        flow_obj.append(table)
        pdf.build(flow_obj)
        messagebox.showinfo('Notifications', 'PDF HAS BEEN SAVED')

    def fifth_pdf(self):
        pagesize = (10 * inch, 10 * inch)
        pdf = SimpleDocTemplate(f"E:\IMS PROJECT\REPORTS\Sales_Data.pdf", pagesize=pagesize)
        flow_obj = []
        # table header

        td = [["S_id", "Name", "Contact_No", "Product_Name","Price","QTY","Discout","GST_18%","GST_28%","Amount","Date"]]

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        data_obj = con.cursor()
        data_obj.execute("select * from sales")
        data_row = data_obj.fetchall()
        for row in data_row:
            data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8],row[9],row[10]]
            td.append(data)
        table = Table(td)

        ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black),
                         # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                         ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
                         ("LEFTPADDING", (0, 0), (-1, -1), 2),
                         ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                         ("BACKGROUND", (0, 1), (-1, -1), colors.white)])

        table.setStyle(ts)
        flow_obj.append(table)
        pdf.build(flow_obj)
        messagebox.showinfo('Notifications', 'PDF HAS BEEN SAVED')


    def employee1(self):
        global counter
        if counter < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = employee.employeeclass(self.new_window)  # employee file objet create  and import the file
            counter += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a employee window!")

    def supplier1(self):

        global c1
        if c1 < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = supplier.supplierclass(self.new_window)  # employee file objet create  and import the file
            c1 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a supplier window!")

    def category1(self):
        global c2
        if c2 < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = category.categoryclass(self.new_window)  # employee file objet create  and import the file
            c2 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a category window!")

    def product1(self):
        global c3
        if c3 < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = product.productclass(self.new_window)  # employee file objet create  and import the file
            c3 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a product window!")
    def sales1(self):
        global c4
        if c4 < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = sales.salesclass(self.new_window)  # employee file objet create  and import the file
            c4 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a sales window!")

    def report1(self):
        global c5
        if c5 < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = reportclass(self.new_window)  # employee file objet create  and import the file
            c5 += 1
        else:
            messagebox.showinfo("Error", "Hey! You've already opened a report window!")

    def dashboard1(self):

        self.root.destroy()
        os.system("python dashoard.py")

    def fetch(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from employee")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', END, values=row)
                con.commit()
            con.close()
    def fetch_1(self):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from supplier")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel_1.delete(*self.tabel_1.get_children())
                for row in rows:
                    self.tabel_1.insert('', END, values=row)
                    con.commit()

            con.close()

    def fetch_2(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from category")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel_2.delete(*self.tabel_2.get_children())
            for row in rows:
                self.tabel_2.insert('', END, values=row)
                con.commit()

        con.close()
    def fetch_3(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from product")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel_4.delete(*self.tabel_4.get_children())
            for row in rows:
                self.tabel_4.insert('', END, values=row)
                con.commit()

        con.close()

    def fetch_4(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from sales")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel_5.delete(*self.tabel_5.get_children())
            for row in rows:
                self.tabel_5.insert('', END, values=row)
                con.commit()

        con.close()




if __name__=="__main__":

    root=Tk()
    obj=reportclass(root)
    root.mainloop()
