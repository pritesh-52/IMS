from tkinter import *
from tkinter import  *
from PIL import Image,ImageTk
from tkinter import  ttk
from tkinter import  messagebox ,filedialog
import mysql.connector as mysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import os
import salesdyw
import  dashoard


class Prediction:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.title("Inventory Management System | Developed By Pritesh Bhatiya")

        title = Label(self.root, text="Sales Prediction",
                      font=('times new roman', 34, 'bold'), bg="#1b0d4c", fg="white", anchor="n", padx=20)
        title.place(x=0, y=2, relwidth=1, height=60)

        lbl_footer = Label(self.root,
                           text="IMS Inventory Management System | Developed By Pritesh Bhatiya \n For Any Quires Contact Us 9033174261",
                           font=('times new roman', 14), bg="#052320", fg="white")
        lbl_footer.place(x=0, y=750, height=50, relwidth=1)

        f5 = Frame(root, relief=RIDGE, bd=2, bg="white")
        f5.place(x=10, y=70, width=450, height=330)

        l1 = Label(f5, text="Sales Data", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 24, 'bold'), justify=CENTER)
        l1.place(relwidth=1)


        data_show = Frame(f5, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(y=45, height=280, relwidth=1, )

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_5 = ttk.Treeview(data_show,
                                    columns=(
                                        "S_id", "Name", "Contact_No", "Product_Name", "Price", "QTY", "Discout", "GST_18%",
                                        "GST_28%", "Amount", "Date"),
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

        lb=Label(root,text="Pie chart of the \n Total product and their Amount",font=('goudy old style',16,'bold'),fg="black",bg="white")
        lb.place(y=70,x=490)
        self.piechart_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#020063",
                                  fg="white", cursor="hand2", command=self.piechart_visualization)
        self.piechart_button.place(x=550, y=140, width=130, height=40)


        lb1 = Label(root, text="Bar plot of the \n Total product and their Amount",
                   font=('goudy old style', 16, 'bold'), fg="black", bg="white")
        lb1.place(y=220, x=490)
        self.barplot_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                      fg="white", cursor="hand2", command=self.barplot_visualization)
        self.barplot_button.place(x=550, y=290, width=130, height=40)

        lb2 = Label(root, text="Line plot of the \n Base price of their final amount",
                    font=('goudy old style', 16, 'bold'), fg="black", bg="white")
        lb2.place(y=70, x=850)

        self.baseprice_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                     fg="white", cursor="hand2", command=self.plot_visualization)
        self.baseprice_button.place(x=900, y=140, width=130, height=40)

        lb3 = Label(root, text="Bar plot of the \n Total sales of the current month",
                    font=('goudy old style', 16, 'bold'), fg="black", bg="white")
        lb3.place(y=220, x=850)
        self.datewise_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#2e0739",
                                     fg="white", cursor="hand2", command=self.datewise_visualization)
        self.datewise_button.place(x=900, y=290, width=130, height=40)

        f4=Frame(relief=RIDGE, bd=2, bg="white")
        f4.place(x=1220,y=70,width=300,height=250)

        lf4= Label(f4, text="Sales Data Date Wise", relief=RIDGE, bd=2, bg="#163332", fg="white",
                   font=('goudy old style', 18, 'bold'), justify=CENTER)
        lf4.place(relwidth=1)

        data_show_1 = Frame(f4, bg="white", borderwidth=2, relief=RIDGE)
        data_show_1.place(y=38, height=210, relwidth=1, )

        scroll_x = x = Scrollbar(data_show_1, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show_1, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_4 = ttk.Treeview(data_show_1,
                                    columns=(
                                        "Date", "Amount"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_4.xview)
        scroll_y.config(command=self.tabel_4.yview)


        self.tabel_4.heading("Date", text="Date")
        self.tabel_4.heading("Amount", text="Amount")
        self.tabel_4['show'] = 'headings'


        self.tabel_4.column("Date", width=150)
        self.tabel_4.column("Amount", width=150)
        self.tabel_4.pack(fill=BOTH, expand=1)
        self.fetch_5()

        self.image1 = Image.open('images/bargraph.jpg')
        self.image1 = self.image1.resize((280, 250), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.new1 = Label(root, image=self.photo1)
        self.new1.place(x=1220,y=340)


        sales_lb=Label(root,text="Distribution of the sales",
                    font=('goudy old style', 18, 'bold'), fg="#072839", bg="white")
        sales_lb.place(x=15,y=410)

        sales_lb_1 = Label(root, text="Distribution of the based on price",
                         font=('goudy old style', 14, 'bold'), fg="black", bg="white")
        sales_lb_1.place(x=15, y=450)

        self.pricebase_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#020063",
                                      fg="white", cursor="hand2", command=self.pricewise_visualization)
        self.pricebase_button.place(x=420,y=445, width=130, height=30)



        sales_lb_2 = Label(root, text="Distribution of the sales based on discount",
                         font=('goudy old style', 14, 'bold'), fg="black", bg="white")
        sales_lb_2.place(x=15, y=495)

        self.discountbase_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                      fg="white", cursor="hand2", command=self.discountbase_visualization)
        self.discountbase_button.place(x=420,y=490, width=130, height=30)


        sales_lb_3 = Label(root, text="Distribution of the sales based on GST18%",
                           font=('goudy old style', 14, 'bold'), fg="black", bg="white")
        sales_lb_3.place(x=15, y=540)

        self.gst18wise_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                          fg="white", cursor="hand2", command=self.gst18wise_visualization)
        self.gst18wise_button.place(x=420, y=540, width=130, height=30)


        sales_lb_4 = Label(root, text="Distribution of the sales based on GST28%",
                           font=('goudy old style', 14, 'bold'), fg="black", bg="white")
        sales_lb_4.place(x=15, y=590)

        self.gst28wise_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#2e0739",
                                       fg="white", cursor="hand2", command=self.gst28wise_visualization)
        self.gst28wise_button.place(x=420, y=595, width=130, height=30)

        self.image2 = Image.open('images/SALES_PREDITION_1.png')
        self.image2 = self.image2.resize((620, 370), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.new2 = Label(root, image=self.photo2)
        self.new2.place(x=580, y=340)

        sales_lb_5 = Label(root, text="Sales forecasting ",
                           font=('goudy old style', 16, 'bold'), fg="black", bg="white")
        sales_lb_5.place(x=840, y=715)

        dashbboard_button = Button(self.root ,text="Dashboard", font=('goudy old style', 16, 'bold'), bg="orange",
                                   fg="black", cursor="hand2", command=self.dashboard1)
        dashbboard_button.place(x=1380, y=20, width=120, height=35)
        dashbboard_button.bind('<Return>', self.dashboard1)
        dashbboard_button.bind('<Button-1>', self.dashboard1)

        sales_lb_6 = Label(root, text="Sales forecasting Yearly, Daywise, Weekly ",
                           font=('goudy old style', 16, 'bold'), fg="black", bg="white")
        sales_lb_6.place(x=15, y=650)
        self.salesydw_button = Button(self.root, text="Show", font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2", command=self.salesydw_visualization)
        self.salesydw_button .place(x=440, y=680, width=130, height=30)

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
    def piechart_visualization(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        df = pd.read_sql(query, con)
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        langs = (df['product_name'])
        plt.title("Pie chart of the Total product and their Amount")
        sales_date = (df['amount'])
        ax.pie(sales_date, labels=langs, autopct='%1.2f%%')
        plt.show()

    def barplot_visualization(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        df = pd.read_sql(query, con)
        fig = plt.figure()
        langs = (df['product_name'])
        sales_date = (df['amount'])
        plt.bar(langs, sales_date, color='g')
        plt.xlabel('PRODUCT NAME')
        plt.ylabel('AMOUNT')
        plt.title("Bar plot of the \n Total product and their Amount")
        plt.show()
    def plot_visualization(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        df = pd.read_sql(query, con)
        fig = plt.figure()
        langs = (df['price'])
        sales_date = (df['amount'])
        plt.plot(langs, sales_date, color='r')
        plt.xlabel('BASE PRICE')
        plt.ylabel('AMOUNT')
        plt.title("Line plot of the \n Base price of their final amount")
        plt.show()
    def datewise_visualization(self):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select date,amount from sales;"
        sales_data = pd.read_sql(query, con)

        data = sales_data.copy()

        data.date = data.date.apply(lambda x: str(x)[:-3])

        data = data.groupby('date')['amount'].sum().reset_index()
        data.date = pd.to_datetime(data.date)
        data.to_csv('monthely_data.csv')

        month_data = pd.read_csv('monthely_data.csv')


        plt.figure(figsize=(6, 6))
        sns.barplot(x='date', y='amount', data=month_data)
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Total sale of the current month')
        plt.show()
    def fetch_5(self):
        with open('monthely_data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                date=row['date']
                amount=row['amount']
                self.tabel_4.insert("",0,values=(date,amount))

    def pricewise_visualization(self):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        sales_data = pd.read_sql(query, con)

        amount = (sales_data['amount'])
        price = (sales_data['price'])
        plt.plot(amount, price, label='Based on total amount price')
        # naming the x axis
        plt.xlabel('Total amount')
        # naming the y axis
        plt.ylabel('Price')
        plt.legend()
        plt.title("Distribution of the based on price")
        plt.show()
        con.close()

    def discountbase_visualization(self):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        sales_data = pd.read_sql(query, con)

        amount = (sales_data['amount'])
        discount= (sales_data['discount'])
        price = (sales_data['price'])
        plt.plot(amount, discount, label='Based on total amount discount')
        plt.plot(price, discount, label='Based on Actual price discount')
        # naming the x axis
        plt.xlabel('Total amount & actual price')
        # naming the y axis
        plt.ylabel('Discount')
        plt.legend()
        plt.title("Distribution of the sales based on discount")
        plt.show()
        con.close()

    def gst18wise_visualization(self):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        sales_data = pd.read_sql(query, con)

        amount = (sales_data['amount'])
        gst18 = (sales_data['gst18'])
        price = (sales_data['price'])
        plt.plot(amount, gst18, label='Based on total amount GST18%')
        plt.plot(price, gst18, label='Based on Actual price GST18%')
        # naming the x axis
        plt.xlabel('Total amount & actual price')
        # naming the y axis
        plt.ylabel('GST18%')
        plt.legend()
        plt.title("Distribution of the sales based on GST18%")
        plt.show()
        con.close()
    def gst28wise_visualization(self):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        query = "select *from sales;"
        sales_data = pd.read_sql(query, con)

        amount=(sales_data['amount'])
        gst28=(sales_data['gst28'])
        qty=(sales_data['qty'])
        price=(sales_data['price'])
        plt.plot(amount,gst28,label='Based on total amount GST28%')
        plt.plot(price,gst28,label='Based on Actual price GST28%')
        # naming the x axis
        plt.xlabel('Total amount & actual price')
        # naming the y axis
        plt.ylabel('GST28%')
        plt.legend()
        plt.title("Distribution of the sales based on GST28%")
        plt.show()
        con.close()

    def salesydw_visualization(self):
        self.new_window = Toplevel(self.root)  # creat top leveal
        self.new_obj = salesdyw.Salesdyw(self.new_window)

    def dashboard1(self, event):
            self.root.destroy()
            os.system("python dashoard.py")








if __name__=="__main__":
    root = Tk()
    obj =Prediction(root)
    root.mainloop()



