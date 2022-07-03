#librarey import
from tkinter import  *
from PIL import Image,ImageTk
from tkcalendar import  *
from tkinter import  ttk
import mysql.connector as mysql
import datetime
from tkinter import  messagebox ,filedialog
import  pandas
from reportlab.pdfgen import canvas

import  employee
import  supplier
import  product
import  category
import dashoard
import reports
import os
from twilio.rest import Client


time = datetime.datetime.now()
timer = str(time.hour)+"hrs : "+str(time.minute)+"mins : "+str(time.second)+" secs"
dateset = str(str(time.day) + '/' + str(time.month) + '/' + str(time.year))



class salesclass:    #main class of the gui windows defined

    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()  # fouce evenet used to focus on the screen
        root.state('zoomed')
        root.config(bg="white")

        root.title("Inventory Management System | Developed By Pritesh Bhatiya")
        root.focus_force()  # fouce evenet used to focus on the screen


        f1=Frame(root,relief=RIDGE,bd=2,bg="white")
        f1.place(x=5,y=10,width=400,height=530)


        l1=Label(f1,text="Products",relief=RIDGE,bd=2,bg="#163332",fg="white",font=('goudy old style',24,'bold'),justify= CENTER)
        l1.place(relwidth=1)


        l2=Label(f1,text="Search Product",bg="white",fg="#ce0a0a",font=('goudy old style',16,'bold'))
        l2.place(y=50,x=10)


        self.var_search_text=StringVar()
        self.txt_search=Entry(f1,textvariable=self.var_search_text,font=('goudy old style',15),bg="lightyellow")
        self.txt_search.place(x=188,y=50,width=200,height=30)

        search_button=Button(f1,text="Search",font=('goudy old style',18,'bold'),bg="#0a5615",fg="white",cursor="hand2",command=self.search_data)
        search_button.place(x=20,y=93,width=150,height=30)
        search_button.bind('<Return>',self.search_data)
        search_button.bind('<Button-1>',self.search_data)

        showall_button=Button(f1,text="Show All",font=('goudy old style',18,'bold'),bg="#0a5615",fg="white",cursor="hand2",command=self.fetch)
        showall_button.place(x=220,y=93,width=150,height=30)






        data_show=Frame(f1,bg="white",borderwidth=2,relief=RIDGE)
        data_show.place(y=140,height=385,relwidth=1,)

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style=ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15,'bold'))
        style.configure("Treeview",font=('times new roman', 12),anchor='CENTER')

        self.tabel= ttk.Treeview(data_show, columns=("Category_Type", "Product_Name", "Price","QTY","Amount"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel.xview)
        scroll_y.config(command=self.tabel.yview)



        self.tabel.heading("Category_Type", text="Category_Type")
        self.tabel.heading("Product_Name", text="Product_Name")
        self.tabel.heading("Price", text="Price")
        self.tabel.heading("QTY",text="QTY")
        self.tabel.heading("Amount",text="Amount")

        self.tabel['show'] = 'headings'



        self.tabel.column("Category_Type", width=150)
        self.tabel.column("Product_Name", width=150)
        self.tabel.column("Price", width=100)
        self.tabel.column("QTY", width=70)
        self.tabel.column("Amount", width=100)

        self.tabel.pack(fill=BOTH, expand=1)
        self.tabel.bind("<ButtonRelease-1>",self.get_data1)
        self.fetch()





        f2=Frame(root,relief=RIDGE,bd=2,bg="white")
        f2.place(x=403,y=10,width=770,height=530)


        l1=Label(f2,text="Customer_Details",relief=RIDGE,bd=2,bg="#163332",fg="white",font=('goudy old style',24,'bold'),justify= CENTER)
        l1.place(relwidth=1)



        self.s_id =Label(f2,text="Sales_Id.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.s_id.place(x=10,y=80)
        self.s_id =StringVar()
        self.s_id.set("No")
        self.entry_s_id =Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.s_id)
        self.entry_s_id .place(x=160,y=85,width=200,height=30)

        self.name =Label(f2,text="Name.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.name .place(x=370,y=80)
        self.name=StringVar()
        self.entry_name=Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.name)
        self.entry_name.place(x=560,y=85,width=200,height=30)

        self.contact_no =Label(f2,text="Contact_No.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.contact_no.place(x=10,y=150)
        self.contact_no =StringVar()
        self.entry_contact_no =Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.contact_no)
        self.entry_contact_no .place(x=160,y=155,width=200,height=30)
        validate_contact = root.register(self.checkcontact)  # validation register
        self.entry_contact_no.config(validate="key", validatecommand=(validate_contact, "%P"))


        self.product_name = Label(f2, text="Product_Name.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.product_name.place(x=370, y=150)
        self.product_name = StringVar()
        self.entry_product_name = Entry(f2, font=('times new roman', 16), bg="lightyellow", textvariable=self.product_name)
        self.entry_product_name.place(x=560, y=155, width=240, height=30)

        self.price =Label(f2,text="Price.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.price.place(x=10,y=220)
        self.price =StringVar()
        self.entry_price =Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.price)
        self.entry_price .place(x=160,y=225,width=200,height=30)
        validate_price = root.register(self.checkprice)  # validation register
        self.entry_price.config(validate="key", validatecommand=(validate_price, "%P"))




        self.qty =Label(f2,text="QTY.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.qty.place(x=370,y=220)
        self.qty =StringVar()
        self.entry_qty=Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.qty)
        self.entry_qty .place(x=560,y=225,width=200,height=30)
        validate_qty = root.register(self.checkqty)  # validation register
        self.entry_qty.config(validate="key", validatecommand=(validate_qty, "%P"))


        self.amount =Label(f2,text="Amount.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.amount.place(x=10,y=290)
        self.amount=StringVar()
        self.entry_amount =Entry(f2,font=('times new roman',16),bg="lightyellow",textvariable=self.amount)
        self.entry_amount .place(x=160,y=295,width=200,height=30)



        self.date =Label(f2,text="Date.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.date.place(x=10,y=405)
        self.date=StringVar()
        self.entry_date =Entry(f2,font=('times new roman',18),bg="lightyellow",textvariable=self.date)
        self.entry_date .place(x=160,y=405,width=200,height=30)
        self.entry_date.insert(END,dateset)

        calculate = Button(f2, text="Calculate",font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                       fg="white", cursor="hand2",command=self.calc)
        calculate.place(x=40, y=345, width=130, height=40)
        calculate.bind('<Return>',self.calc)
        calculate.bind('<Button-1>', self.calc)



        save_button = Button(f2, text="Add",font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2",command=self.add_data)
        save_button.place(x=30, y=470, width=130, height=40)
        save_button.bind('<Return>', self.add_data)
        save_button.bind('<Button-1>', self.add_data)

        update_button = Button(f2, text="Update", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                     fg="white", cursor="hand2",command=self.update)
        update_button.place(x=220, y=470, width=130, height=40)
        update_button.bind('<Return>', self.update)
        update_button.bind('<Button-1>', self.update)

        delete_button = Button(f2, text="Delete", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                       fg="white",cursor="hand2",command=self.delete)
        delete_button.place(x=410, y=470, width=130, height=40)
        delete_button.bind('<Return>', self.delete)
        delete_button.bind('<Button-1>', self.delete)

        clear_button = Button(f2, text="Clear", font=('goudy old style', 20, 'bold'), bg="#052320",
                                      fg="white", cursor="hand2",command=self.clear)
        clear_button.place(x=600, y=470, width=130, height=40)
        clear_button.bind('<Return>', self.clear)
        clear_button.bind('<Button-1>', self.clear)


        self.image2=Image.open('images/supply.jpg')
        self.image2=self.image2.resize((350,150), Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(self.image2)
        self.new2 = Label(root,image=self.photo2,relief=SOLID,borderwidth=2)
        self.new2.place(x=800,y=280)



        word_lable=Label(f2,text="W_orldwide S_upply",font=('Microsoft Sans Serif',22,'bold'),bg="white",fg="black",bd=3)
        word_lable.place(x=420,y=425)




        f3=Frame(root,relief=RIDGE,bd=2,bg="white")
        f3.place(x=1170,y=10,width=360,height=530)


        l3=Label(f3,text="Search_Sales_Detail",bg="white",fg="#ce0a0a",font=('goudy old style',17,'bold'))
        l3.place(y=8)




        dashbboard_button = Button(f3, text="Dashboard", font=('goudy old style', 16, 'bold'), bg="#163332",
                                    fg="white",cursor="hand2",command=self.dashboard1)
        dashbboard_button.place(x=235,y=5, width=120, height=35)
        dashbboard_button.bind('<Return>', self.dashboard1)
        dashbboard_button.bind('<Button-1>', self.dashboard1)


        self.var_search_by_1=StringVar()
        self.cmb_search_1=ttk.Combobox(f3,values=("Select","S_id","Date"),state='readonly',textvariable=self.var_search_by_1,justify=CENTER,font=('times new roman',16))   #create combo box
        self.cmb_search_1.place(x=5,y=53,width=180)
        self.cmb_search_1.current(0)

        self.var_search_text_1=StringVar()
        self.txt_search_1=Entry(f3,textvariable=self.var_search_text_1,font=('goudy old style',15),bg="lightyellow")
        self.txt_search_1.place(x=200,y=53,width=150,height=30)


        search_button=Button(f3,text="Search",font=('goudy old style',18,'bold'),bg="#0a5615",fg="white",cursor="hand2",command=self.search_data_1)
        search_button.place(x=10,y=100,width=160,height=35)
        search_button.bind('<Return>',self.search_data_1)
        search_button.bind('<Button-1>', self.search_data_1)

        showall_button=Button(f3,text="Show All",font=('goudy old style',18,'bold'),bg="#0a5615",fg="white",cursor="hand2",command=self.fetch_1)
        showall_button.place(x=185,y=100,width=160,height=35)
        showall_button.bind('<Return>',self.all_show_2)
        showall_button.bind('<Button-1>', self.all_show_2)



        data_show_1=Frame(f3,bg="white",borderwidth=2,relief=RIDGE)
        data_show_1.place(y=150,height=373,relwidth=1,)

        scroll_x = x1 = Scrollbar(data_show_1, orient=HORIZONTAL)
        scroll_y = y1 = Scrollbar(data_show_1, orient=VERTICAL)

        style=ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15,'bold'))
        style.configure("Treeview",font=('times new roman', 12),anchor='CENTER')

        self.tabel_1 = ttk.Treeview(data_show_1, columns=("S_id","Name","Contact_No","Product_Name","Price","QTY","Discout","GST_18%","GST_28%","Amount","Date"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_1.xview)
        scroll_y.config(command=self.tabel_1.yview)


        self.tabel_1.heading("S_id", text="S_id")
        self.tabel_1.heading("Name", text="Name")
        self.tabel_1.heading("Contact_No", text="Contact_No")
        self.tabel_1.heading("Product_Name", text="Product_Name")
        self.tabel_1.heading("Price",text="Price")
        self.tabel_1.heading("QTY",text="QTY")
        self.tabel_1.heading("Discout",text="Discout")
        self.tabel_1.heading("GST_18%",text="GST_18%")
        self.tabel_1.heading("GST_28%",text="GST_28%")
        self.tabel_1.heading("Amount",text="Amount"),
        self.tabel_1.heading("Date",text="Date")
        self.tabel_1['show'] = 'headings'


        self.tabel_1.column("S_id", width=70)
        self.tabel_1.column("Name", width=150)
        self.tabel_1.column("Contact_No", width=150)
        self.tabel_1.column("Product_Name", width=150)
        self.tabel_1.column("Price", width=70)
        self.tabel_1.column("QTY", width=100)
        self.tabel_1.column("Discout", width=100)
        self.tabel_1.column("GST_18%", width=100)
        self.tabel_1.column("GST_28%", width=100)
        self.tabel_1.column("Amount", width=100),
        self.tabel_1.column("Date", width=100),

        self.tabel_1.pack(fill=BOTH, expand=1)
        self.tabel_1.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_1()


        f4=Frame(root,relief=RIDGE,bd=2,bg="white")
        f4.place(x=5,y=545,width=430,height=248)
        bill_title = Label(f4,text="Inventory management system", font=('goudy old styl=',18,'bold'),bg="#163332",fg="white").pack(fill=X)
        scrol_y = Scrollbar(f4, orient=VERTICAL)
        self.txtarea = Text(f4, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()
        self.txtarea.pack(fill=BOTH, expand=1)


        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tSales Bill \n")
        self.txtarea.insert(END, f"\n Bill Number :-{self.s_id.get()} \t\t\t Date :-{self.s_id.get()}")
        self.txtarea.insert(END, f"\n Customer Name:-{self.name.get()}")
        self.txtarea.insert(END, f"\n Phone number:-{self.contact_no.get()}")
        self.txtarea.insert(END, f"\n =================================================")
        self.txtarea.insert(END, f"\n ProductsName")
        self. txtarea.insert(END, f"\n Price")
        self. txtarea.insert(END, f"\n QTY")
        self.txtarea.insert(END, f"\n =================================================")
        self.txtarea.insert(END, f"\n Discount Price")
        self.txtarea.insert(END, f"\n GST Price 18%")
        self.txtarea.insert(END, f"\n GST Price 28%")
        self.txtarea.insert(END, f"\n Total Price")
        self.txtarea.insert(END, f"\n =================================================")


        rightmenu=Frame(root,relief=RIDGE,bd=2,bg="white")
        rightmenu.place(x=1385,y=545,width=140,height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")

        btn_employee=Button(rightmenu,text="Employee",image=self.right_arrow,compound=LEFT,padx=5,anchor="w",font=('times new roman',14,'bold'),bg="white",bd=3,command=self.employee1,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)


        btn_supplier = Button(rightmenu, text="Supplier", image=self.right_arrow,compound=LEFT,padx=5, anchor="w",font=('times new roman', 14, 'bold'), bg="white", bd=3,command=self.supplier1, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)


        btn_category = Button(rightmenu, text="Category", image=self.right_arrow,compound=LEFT, padx=5, anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3,command=self.category1, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)


        btn_product = Button(rightmenu, text="Product",image=self.right_arrow, compound=LEFT,padx=5, anchor="w",
                                      font=('times new roman', 14, 'bold'),command=self.product1, bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)


        btn_sales = Button(rightmenu, text="Sales", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                                     font=('times new roman', 14, 'bold'), command=self.sales1,bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)


        btn_purchase = Button(rightmenu, text="Report", image=self.right_arrow,compound=LEFT, padx=5, anchor="w",
                                   font=('times new roman',14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.report1)
        btn_purchase.pack(side=TOP, fill=X)




        self.amount_1 =Label(root,text="Amount.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.amount_1.place(x=450,y=560)
        self.amount_1=StringVar()
        self.entry_amount_1 =Entry(root,font=('times new roman',18),bg="lightyellow",textvariable=self.amount_1)
        self.entry_amount_1 .place(x=650,y=560,width=200,height=30)



        self.discount=Label(root,text="Discount.",fg="black",font=('goudy old style',18,'bold'),bg="white")
        self.discount.place(x=450,y=610)
        self.discount=IntVar()
        self.entry_discount=Entry(root,font=('times new roman',18),bg="lightyellow",textvariable=self.discount)
        self.entry_discount .place(x=650,y=610,width=200,height=30)



        self.gst_18=Label(root,text="GST 18%.",fg="black",font=('goudy old style',18,'bold'),bg="white")
        self.gst_18.place(x=450,y=660)
        self.gst_18=IntVar()
        self.gst_18_entry=Entry(root,font=('times new roman',18),bg="lightyellow",textvariable=self.gst_18)
        self.gst_18_entry.place(x=650,y=660,width=200,height=30)



        self.gst_28=Label(root,text="GST 28%.",fg="black",font=('goudy old style',18,'bold'),bg="white")
        self.gst_28.place(x=450,y=710)
        self.gst_28=IntVar()
        self.gst_28_entry=Entry(root,font=('times new roman',18),bg="lightyellow",textvariable=self.gst_28)
        self.gst_28_entry.place(x=650,y=710,width=200,height=30)






        self.total_amount=Label(root,text="Total_Amount.",fg="black",font=('goudy old style',18,'bold'),bg="white")
        self.total_amount.place(x=450,y=760)
        self.total_amount=StringVar()
        self.entry_total_amount=Entry(root,font=('times new roman',18),bg="lightyellow",textvariable=self.total_amount)
        self.entry_total_amount .place(x=650,y=760,width=200,height=30)

        t_lable=Label(root,text="Include of all taxes",fg="black",font=('goudy old style',8),bg="white")
        t_lable.place(x=450,y=785)




        discount_button = Button(root, text="Discount 5%",font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                       fg="white", cursor="hand2",command=self.dis)
        discount_button.place(x=900, y=560, width=200, height=40)
        '''discount_button.bind('<Return>',self.dis)
        discount_button.bind('<Button-1>', self.dis)'''



        gst18_button = Button(root, text="GST 18%",font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2",command=self.gst18)
        gst18_button.place(x=900, y=620, width=200, height=40)
        '''gst18_button.bind('<Return>', self.gst18)
        gst18_button.bind('<Button-1>', self.gst18)'''


        gst28_button = Button(root, text="GST 28%",font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2",command=self.gst28)
        gst28_button.place(x=900, y=680, width=200, height=40)
        '''gst28_button.bind('<Return>', self.gst28)
        gst28_button.bind('<Button-1>', self.gst28)'''



        genrate_bill = Button(root, text="Generate Bill",font=('goudy old style', 20, 'bold'), bg="#db0909",
                                       fg="white", cursor="hand2",command=self.genrate_bill)
        genrate_bill.place(x=900, y=740, width=200, height=40)
        '''genrate_bill.bind('<Return>', self.genrate_bill)
        genrate_bill.bind('<Button-1>', self.genrate_bill)'''






        export_button = Button(root, text="Export_Data",font=('goudy old style', 20, 'bold'), bg="crimson",
                                       fg="white", cursor="hand2",command=self.export)
        export_button.place(x=1140, y=560, width=200, height=40)
        '''export_button.bind('<Return>', self.export)
        export_button.bind('<Button-1>', self.export)'''

        self.image3 = Image.open('images/salesgrow.jpg')
        self.image3= self.image3.resize((250, 150), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.new3 = Label(root, image=self.photo3, relief=SOLID, borderwidth=2)
        self.new3.place(x=1120 ,y=610)

        ims=Label(root,text="IMS",font=('times new roman',18,'bold'),fg="black",bg="white")
        ims.place(x=1330,y=755)


        r1 = Frame(root, bg="red")
        r1.place(x=1270, y=785, height=10, width=15)

        r2 = Frame(root, bg="orange")
        r2.place(x=1300, y=785, height=10, width=15)

        r3 = Frame(root, bg="#32cd32")
        r3.place(x=1330, y=785, height=10, width=15)

        r4 = Frame(root, bg="#00008b")
        r4.place(x=1360, y=785, height=10, width=15)

        self.root.bind("<Escape>", exit)
        self.root.bind('<Delete>', self.delete)

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

    def add_data(self,event):
            global rows


            name = self.entry_name.get()
            contact_no =self. entry_contact_no.get()
            product_name = self.entry_product_name.get()
            price = self.entry_price.get()
            qty = self.entry_qty.get()
            discount = self.entry_discount.get()
            gst_18 = self.gst_18_entry.get()
            gst_28 = self.gst_28_entry.get()
            amount = self.entry_amount.get()
            date = self.entry_date.get()

            if (
                    name == "" or contact_no == "" or product_name == "" or price == "" or qty == "" or amount == "" or date == ""):
                messagebox.showerror("Insert Status", "ALL FILEDS ARE REQUIRED")
            elif len(contact_no) < 10:
                messagebox.showerror("Error", "Contact Number Should Be 10 Character")
            elif len(contact_no) > 10:
                messagebox.showerror("Error", "Contact Number Only 10 Character")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                # cursor.execute("insert into employee values('" + emp_id + "','" + gender + "','" + contact_no + "','" + name + "','" + dob + "','" + doj + "','" + email + "','" + password + "','" + user_type + "','" + address + "'," + salary + "')")
                cursor.execute(
                    'INSERT INTO sales(name, contact_no, product_name, price, qty, discount, gst18, gst28,amount,date )VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (name, contact_no, product_name, price, qty, discount, gst_18, gst_28, amount, date))
                cursor.execute("commit")

                self.entry_name.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.entry_product_name.delete(0, 'end')
                self.entry_price.delete(0, 'end')
                self.entry_qty.delete(0, 'end')
                self.entry_discount.delete(0, 'end')
                self.gst_18_entry.delete(0, 'end')
                self.gst_28_entry.delete(0, 'end')
                self.entry_amount.delete(0, 'end')
                self.entry_total_amount.delete(0,'end')
                self.entry_amount_1.delete(0,'end')

                self.fetch_1()
                #self.clear()
                messagebox.showinfo("Insert Status", "Insert SucessFUlly")
                con.close()

    def genrate_bill(self):
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\t\tSales Bill \n")
            self.txtarea.insert(END, f"\n Bill Number :-{self.s_id.get()} \t\t\t Date :-{self.entry_date.get()}")
            self.txtarea.insert(END, f"\n Customer Name:-{self.entry_name.get()}")
            self.txtarea.insert(END, f"\n Phone number:-{self.entry_contact_no.get()}")
            self.txtarea.insert(END, f"\n =================================================")
            self.txtarea.insert(END, f"\n ProductsName:-{self.entry_product_name.get()}")
            self.txtarea.insert(END, f"\n Price:-{self.entry_price.get()}")
            self.txtarea.insert(END, f"\n QTY:-{self.entry_qty.get()}")
            self.txtarea.insert(END, f"\n =================================================")
            self.txtarea.insert(END, f"\n Discount Price:{self.discount.get()}")
            self.txtarea.insert(END, f"\n GST Price 18%:{self.gst_18.get()}")
            self.txtarea.insert(END, f"\n GST Price 28%:{self.gst_28.get()}")
            self.txtarea.insert(END, f"\n Total Price:{self.entry_amount.get()}")
            self.txtarea.insert(END, f"\n =================================================")


            c = canvas.Canvas(f"E:\IMS PROJECT\BILLS\{self.s_id.get()}.pdf", pagesize=(200, 250), bottomup=0)

            # Logo Section
            # Setting th origin to (10,40)
            c.translate(10, 40)
            # Inverting the scale for getting mirror Image of logo
            c.scale(1, -1)
            # Inserting Logo into the Canvas at required position
            c.drawImage("logo.jpg", 0, 0, width=50, height=30)

            # Title Section
            # Again Inverting Scale For strings insertion
            c.scale(1, -1)
            # Again Setting the origin back to (0,0) of top-left
            c.translate(-10, -40)
            # Setting the font for Name title of company
            c.setFont("Helvetica-Bold", 10)
            # Inserting the name of the company
            c.drawCentredString(125, 20, "XYZ PRIVATE LIMITED")
            # For under lining the title
            c.line(70, 22, 180, 22)
            # Changing the font size for Specifying Address
            c.setFont("Helvetica-Bold", 5)
            c.drawCentredString(125, 30, "Rukhdiya Hanumanji Near Moti Studio,")
            c.drawCentredString(125, 35, "Bhavnagar - 364001, ,Gujrat,India")
            # Changing the font size for Specifying GST Number of firm
            c.setFont("Helvetica-Bold", 6)
            c.drawCentredString(125, 42, "GSTIN : 07AABCS1429B1Z")

            # Line Seprating the page header from the body
            c.line(5, 45, 195, 45)

            # Document Information
            # Changing the font for Document title
            c.setFont("Courier-Bold", 8)
            c.drawCentredString(100, 55, "TAX-INVOICE")

            # This Block Consist of Costumer Details
            c.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)
            c.setFont("Times-Bold", 5)
            c.drawRightString(70, 70, f"INVOICE No.  {self.s_id.get()}")
            c.drawRightString(70, 80, f"DATE :   {self.entry_date.get()}")
            c.drawRightString(79, 90, "CUSTOMER NAME:")
            c.drawCentredString(110,90,self.entry_name.get())
            c.drawRightString(58, 100, "PHONE No.")
            c.drawCentredString(74, 100, self.entry_contact_no.get())

            # This Block Consist of Item Description
            c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
            c.line(15, 120, 185, 120)
            c.drawCentredString(25, 118, "SR No.")
            c.drawCentredString(75, 118, "PRODUCT_NAME")
            c.drawCentredString(125, 118, "RATE")
            c.drawCentredString(148, 118, "QTY")
            c.drawCentredString(173, 118, "TOTAL")
            # Drawing table for Item Description
            c.line(15, 210, 185, 210)

            c.line(35, 108, 35, 220)

            c.line(115, 108, 115, 220)
            c.line(135, 108, 135, 220)
            c.line(160, 108, 160, 220)

            c.drawCentredString(20, 130, "1")
            self.n8=IntVar()
            self.n8.set(self.entry_price.get())
            self.n9=IntVar()
            self.n9.set(self.entry_qty.get())
            self.n10=StringVar()
            self.n10.set(int(self.n8.get())*int(self.n9.get()))
            self.n8.set(int(self.entry_price.get()) * int(self.entry_qty.get()))
            c.drawCentredString(70, 130, self.entry_product_name.get())
            c.drawCentredString(125, 130, self.entry_price.get())
            c.drawCentredString(150,130, self.entry_qty.get())
            c.drawCentredString(170, 130,self.n10.get())
            self.n11=StringVar()
            self.n11.set(int(self.discount.get()))
            c.drawCentredString(95,193,"Discount Price:")
            c.drawCentredString(170,193,self.n11.get())

            self.n12 = StringVar()
            self.n12.set(int(self.gst_18.get()))
            c.drawCentredString(95, 200, "GST 18%:")
            c.drawCentredString(170, 200, self.n12.get())

            self.n13 = StringVar()
            self.n13.set(int(self.gst_28.get()))
            c.drawCentredString(95, 207, "GST 28%:")
            c.drawCentredString(170, 207, self.n13.get())


            c.drawCentredString(95, 217, "Total Amount:")
            c.drawCentredString(170, 217, self.entry_total_amount.get())




            # Declaration and Signature
            c.line(15, 220, 185, 220)
            c.line(100, 220, 100, 238)
            c.drawString(20, 225, "We declare that above mentioned")
            c.drawString(20, 230, "information is true.")
            c.drawString(20, 235, "(This is system generated invoive)")
            c.drawRightString(180, 235, "Authorised Signatory")

            # End the Page and Start with new
            c.showPage()
            # Saving the PDF
            c.save()
            messagebox.showinfo("info", "Bill Genrated")
            sid = 'AC29f9b9c407da027d843e72d3522b9037'
            auth_token = 'fc9b90a690401db8dd2b9f8435cf9549'

            try:
                client = Client(sid, auth_token)
                resp = client.messages.create(body=f"Name:- {self.name.get()}"
                                                   f"\n Product Name:- {self.product_name.get()}"
                                                   f"\n Product Price:- ₹{self.price.get()}"
                                                   f"\n Total QTY:- {self.qty.get()}"
                                                   f"\n Total Discount Price:- ₹{self.discount.get()}"
                                                   f"\n GST 18% Price:- ₹{self.gst_18.get()}"
                                                   f"\n GST 28% Price:- ₹{self.gst_28.get()}"
                                                   f"\n Total Payable Amount:-₹{self.total_amount.get()} ", from_="+19034965997", to=f"+91{self.contact_no.get()}")
                print(resp.sid)
            except:
                 print("number not register")

    def checkcontact(self,con):
        if con.isdigit():
            return True
        if len(str(con)) == 0:
            return True


        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False

    def update(self,event):
            s_id = self.entry_s_id.get()
            name = self.entry_name.get()
            contact_no = self.entry_contact_no.get()
            product_name = self.entry_product_name.get()
            price = self.entry_price.get()
            qty = self.entry_qty.get()
            discount = self.entry_discount.get()
            gst_18 = self.gst_18_entry.get()
            gst_28 = self.gst_28_entry.get()
            amount = self.entry_amount.get()
            date = self.entry_date.get()

            if (
                    s_id == "" or name == "" or contact_no == "" or product_name == "" or price == "" or qty == "" or amount == "" or date == ""):
                messagebox.showerror("Update Status", "All Flieds Are Requried")
            elif len(contact_no) < 10:
                messagebox.showerror("Error", "Contact Number Should Be 10 Character")
            elif len(contact_no) > 10:
                messagebox.showerror("Error", "Contact Number Only 10 Character")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                cursor.execute(
                    "update sales set name='" + name + "', contact_no ='" + contact_no + "',product_name='" + product_name + "', price='" + price + "',qty='" + qty + "',discount='" + discount + "',gst18='" + gst_18 + "',gst28='" + gst_28 + "',amount='" + amount + "', date='" + date + "' where  s_id='" + s_id + "'")
                cursor.execute("commit")

                self.entry_name.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.entry_product_name.delete(0, 'end')
                self.entry_price.delete(0, 'end')
                self.entry_qty.delete(0, 'end')
                self.entry_discount.delete(0, 'end')
                self.gst_18_entry.delete(0, 'end')
                self.gst_28_entry.delete(0, 'end')
                self.entry_amount.delete(0, 'end')
                self.entry_amount_1.delete(0,'end')
                self.entry_total_amount.delete(0,'end')

                self.fetch_1()
                messagebox.showinfo("Update Status", "Updated SucessFully")
                con.close()

    def clear(self,event):
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("commit")
            self.s_id.set("No")
            self.entry_name.delete(0, 'end')
            self.entry_contact_no.delete(0, 'end')
            self.entry_product_name.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_amount.delete(0, 'end')

            self.entry_amount_1.delete(0, 'end')
            self.entry_discount.delete(0, 'end')
            self.gst_18_entry.delete(0, 'end')
            self.gst_28_entry.delete(0, 'end')
            self.entry_total_amount.delete(0, 'end')
            messagebox.showinfo("Inform", "Data will be clear")
            con.close()

    def delete(self,event):
            if (self.entry_s_id.get() == ""):
                messagebox.showerror("Delete", "Delete Requried")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                cursor.execute("delete from sales where s_id='" + self.entry_s_id.get() + "'")
                cursor.execute("commit")

                self.s_id.set("No")
                self.entry_name.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.entry_product_name.delete(0, 'end')
                self.entry_price.delete(0, 'end')
                self.entry_qty.delete(0, 'end')
                self.entry_amount.delete(0, 'end')
                self.entry_discount.delete(0,'end')
                self.gst_18_entry.delete(0,'end')
                self.gst_28_entry.delete(0,'end')
                self.entry_amount_1.delete(0,'end')
                self.entry_total_amount.delete(0,'end')


                self.fetch_1()
                messagebox.showinfo("Delete Status", "Delete SucessFully")
                con.close()
    def export(self):
            file = filedialog.asksaveasfilename()
            get = self.tabel_1.get_children()
            first, second, third, four, fifth, six, seven, eight, nine, ten, eleven = [], [], [], [], [], [], [], [], [], [], []
            for i in get:
                content = self.tabel_1.item(i)
                val = content['values']
                first.append(val[0]), second.append(val[1]), third.append(val[2]), four.append(val[3]), fifth.append(
                    val[4]), six.append(val[5]), seven.append(val[6]), eight.append(val[7]), nine.append(
                    val[8]), ten.append(val[9]), eleven.append(val[10])
                seven.append(val[6]), eight.append(val[7])
            dd = ['S_id', 'Name', 'Contact_No', 'Product_Name', 'Price', 'QTY', 'Discout', 'GST_18%', 'GST_28%',
                  'Amount', 'Date']
            df = pandas.DataFrame(list(zip(first, second, third, four, fifth, six, seven, eight, nine, ten, eleven)),
                                  columns=dd)
            paths = r'{}.csv'.format(file)
            df.to_csv(paths, index=False)
            messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

    def dis(self):

            self.var = IntVar()
            self.var.set(5)
            self.var1 = IntVar()
            self.var1.set(100)
            self.var3=IntVar()
            self.var3.set(self.amount.get())
            self. amount_1.set(int(self.price.get()) * int(self.qty.get()))
            self.discount.set(int(self.amount_1.get()) * self.var.get() / self.var1.get())
            self.amount.set(int(self.var3.get())-int(self.discount.get()))


    def gst18(self):

            self.var2 = IntVar()
            self.var2.set(18)
            self.var3 = IntVar()
            self.var3.set(100)

            self.n1 = IntVar()
            self.n1.set(int(self.amount_1.get()) - int(self.discount.get()))
            self.gst_18.set(int(self.n1.get()) * int(self.var2.get()) / int(self.var3.get()))

            if (self.discount.get() == ""):
                self.total_amount.set(int(self.amount_1.get()) + int(self.gst_18.get()))
                self.amount.set(int(self.amount_1.get()) + int(self.gst_18.get()))
            else:
                self.total_amount.set(int(self.amount_1.get()) - int(self.discount.get()) + int(self.gst_18.get()))
                self.amount.set(int(self.amount_1.get()) - int(self.discount.get()) + int(self.gst_18.get()))
                self. gst_28.set(0)

    def gst28(self):
            self.var4 = IntVar()
            self.var4.set(28)
            self.var5 = IntVar()
            self.var5.set(100)

            self.n2 = IntVar()
            self.n2.set(int(self.amount_1.get()) - int(self.discount.get()))
            self.gst_28.set(int(self.n2.get()) * int(self.var4.get()) / int(self.var5.get()))

            if (self.discount.get() == ""):
                self.total_amount.set(int(self.amount_1.get()) + int(self.gst_28.get()))
                self. amount.set(int(self.amount_1.get()) + int(self.gst_28.get()))
            else:
                self.total_amount.set(int(self.amount_1.get()) - int(self.discount.get()) + int(self.gst_28.get()))
                self.amount.set(int(self.amount_1.get()) - int(self.discount.get()) + int(self.gst_28.get()))
                self.gst_18.set(0)

    def calc(self,event):
            self.amount.set(int(self.price.get()) * int(self.qty.get()))
            self.amount_1.set(int(self.price.get()) * int(self.qty.get()))
            messagebox.showinfo("info","Amount calculate")

    def search_data_1(self,event):

            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from sales where " + str(self.var_search_by_1.get()) + " LIKE '%" + str(
                self. var_search_text_1.get()) + "%'")
            self.cmb_search_1.current(0)
            self.txt_search_1.delete(0, 'end')
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel_1.delete(*self.tabel_1.get_children())
                for row in rows:
                    self.tabel_1.insert('', END, values=row)
                    con.commit()
                messagebox.showinfo("info", "data will be found")
                con.close()
            else:
                messagebox.showerror("Error", "data will be not  found")

    def get_data(self,event):
            cur = self.tabel_1.focus()
            left = self.tabel_1.item(cur)
            row = left['values']


            self.s_id.set(row[0])
            self.name.set(row[1])
            self.contact_no.set(row[2])
            self.product_name.set(row[3])
            self.price.set(row[4])
            self.qty.set(row[5])
            self.discount.set(row[6])
            self.gst_18.set(row[7])
            self.gst_28.set(row[8])
            self.amount.set(row[9])
            self.amount_1.set(row[9])
            self.total_amount.set(row[9])
            self.date.set(row[10])

    def get_data1(self,event):
            cur = self.tabel.focus()
            left = self.tabel.item(cur)
            row = left['values']

            self.product_name.set(row[1])
            self.price.set(row[2])
            self.qty.set(row[3])
            self.amount.set(row[4])
            self.amount_1.set(row[4])

    def fetch_1(self):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from sales")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel_1.delete(*self.tabel_1.get_children())
                for row in rows:
                    self.tabel_1.insert('', END, values=row)
                    con.commit()

            con.close()
    def all_show_2(self,event):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from sales")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel_1.delete(*self.tabel_1.get_children())
                for row in rows:
                    self.tabel_1.insert('', END, values=row)
                    con.commit()
            con.close()
            messagebox.showinfo("info", "All data in the display")


    def checkprice(self, con):
        if con.isdigit():
            return True
        if len(str(con)) == 0:
            return True


        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False

    def checkqty(self, con):
        if con.isdigit():
            return True
        if len(str(con)) == 0:
            return True


        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False

    def fetch(self):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select category_type,product_name,price,qty,amount from product ")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()

            con.close()

    '''def all_show(self,event):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select ")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()
                    con.close()
                    messagebox.showinfo("info", "All data in the display")


    #messagebox.showinfo("info", "All data in the display")'''

    def search_data(self,event):

            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from product where p_id LIKE '%" + str(self.var_search_text.get()) + "%'")

            self.txt_search.delete(0, 'end')
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()
                messagebox.showinfo("info", "data will be found")
                con.close()
            else:
                messagebox.showerror("Error", "data will be not  found")

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
        if c4 < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = salesclass(self.new_window)  # employee file objet create  and import the file
            c4 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a sales window!")

    def dashboard1(self,event):

        self.root.destroy()
        os.system("python dashoard.py")

    def report1(self):
        global c5
        if c5 < 2:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = reports.reportclass(self.new_window)  # employee file objet create  and import the file
            c5 += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a report window!")

if __name__=="__main__":

    root=Tk()
    obj=salesclass(root)
    root.mainloop()