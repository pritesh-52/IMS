#librarey import
from tkinter import  *
from PIL import Image,ImageTk
from tkcalendar import  *
from tkinter import  ttk
from  tkcalendar import DateEntry
from tkinter import  messagebox ,filedialog
import mysql.connector as mysql
import  pandas
import os



import  employee
import  category
import  product
import  sales
import  dashoard
import reports



class supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()  # fouce evenet used to focus on the screen


        root.state('zoomed')
        root.config(bg="white")

        root.title("Inventory Management System | Developed By Pritesh Bhatiya")

        root.focus_force()

        seacrhframe=LabelFrame(root,text="Search Invoice",bg="white",font=('goudy old style',16,'bold'),bd=2,relief=RIDGE)
        seacrhframe.place(x=50,y=25,width=950,height=90)
        self.var_search_by=StringVar()
        self.cmb_search=ttk.Combobox(seacrhframe,values=("Select","invoice_no","supplier_name"),state='readonly',textvariable=self.var_search_by,justify=CENTER,font=('times new roman',16))   #create combo box
        self.cmb_search.place(x=30,y=15,width=200)
        self.cmb_search.current(0)

        self.var_search_text=StringVar()
        self.txt_search=Entry(seacrhframe,textvariable=self.var_search_text,font=('goudy old style',15),bg="lightyellow")
        self.txt_search.place(x=270,y=15,width=250,height=30)

        search_button=Button(seacrhframe,text="Search",font=('goudy old style',18,'bold'),bg="#4caf50",fg="white",cursor="hand2",command=self.search_data)
        search_button.place(x=550,y=15,width=180,height=35)
        search_button.bind('<Return>', self.search_data)
        search_button.bind('<Button-1>', self.search_data)

        showall_button=Button(seacrhframe,text="Show All",font=('goudy old style',18,'bold'),bg="#4caf50",fg="white",cursor="hand2",command=self.fetch)
        showall_button.place(x=750,y=15,width=180,height=35)
        showall_button.bind('<Return>', self.all_show)
        showall_button.bind('<Button-1>', self.all_show)


        self.image1=Image.open('images/supplier.jpg')
        self.image1=self.image1.resize((280,150), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(self.image1)
        self.new1 = Label(root,image=self.photo1,relief=SOLID,borderwidth=4)
        self.new1.place(x=1100)

        dashbboard_button = Button(root, text="Dashboard", font=('goudy old style', 16, 'bold'), bg="#052320",
                                    fg="white",cursor="hand2",command=self.dashboard1)
        dashbboard_button.place(x=1400,y=40, width=120, height=35)
        dashbboard_button.place(x=1400, y=40, width=120, height=35)
        dashbboard_button.bind('<Return>', self.dashboard1)
        dashbboard_button.bind('<Button-1>', self.dashboard1)



        title=Label(root,text="Supplier Details",font=('goudy old style',20,'bold'),bg="#0f4d7d",fg="white")
        title.place(x=0,y=130,relwidth=1)


#1
        self.invoice_no =Label(root,text="Invoice_no.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.invoice_no .place(x=40,y=190)
        self.invoice_no=StringVar()
        self.entry_invoice_no =Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.invoice_no)
        self.entry_invoice_no .place(x=270,y=195,width=240,height=30)

#2
        self.supplier_name = Label(root, text="Supplier_name.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.supplier_name.place(x=570, y=190)
        self.supplier_name=StringVar()
        self.entry_supplier_name=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.supplier_name)
        self.entry_supplier_name.place(x=800,y=195,width=240,height=30)



#4
        self.gst_number=Label(root,text="GST_Number.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.gst_number.place(x=40,y=250)
        self.gst_number=StringVar()
        self.entry_gst_number=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.gst_number)
        self.entry_gst_number.place(x=270,y=255,width=240,height=30)

#5
        self.contact_no=Label(root,text="Contact_no.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.contact_no.place(x=570,y=250)
        self.contact_no=StringVar()
        self.entry_contact_no=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.contact_no)
        self.entry_contact_no.place(x=800,y=255,width=240,height=30)
        validate_contact = root.register(self.checkcontact)  # validation register
        self.entry_contact_no.config(validate="key", validatecommand=(validate_contact, "%P"))


        self.supply_product=Label(root,text="Supply_product.",font=('goudy old style',18,'bold'),fg="black",bg="white")
        self.supply_product.place(x=40,y=310)
        self.supply_product=StringVar()
        self.entry_supply_product=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.supply_product)
        self.entry_supply_product.place(x=270,y=315,width=240,height=30)


        self.price=Label(root,text="Price.",font=('goudy old style',18,'bold'),fg="black",bg="white")
        self.price.place(x=570,y=310)
        self.price=StringVar()
        self.entry_price=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.price)
        self.entry_price.place(x=800,y=315,width=240,height=30)
        validate_price = root.register(self.checkprice)  # validation register
        self.entry_price.config(validate="key", validatecommand=(validate_price, "%P"))



        self.qty=Label(root,text="QTY.",font=('goudy old style',18,'bold'),fg="black",bg="white")
        self.qty.place(x=40,y=370)
        self.qty=StringVar()
        self.entry_qty=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.qty)
        self.entry_qty.place(x=270,y=375,width=240,height=30)
        validate_qty = root.register(self.checkqty)  # validation register
        self.entry_qty.config(validate="key", validatecommand=(validate_qty, "%P"))


        self.other_information =Label(root,text="Other_Information.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.other_information.place(x=570,y=370)
        self.other_information=StringVar()
        self.entry_other_information = Entry(root, font=('times new roman',16), bg="lightyellow",textvariable=self.other_information)
        self.entry_other_information.place(x=800, y=375, width=330, height=80)


        self.image2=Image.open('images/supply.jpg')
        self.image2=self.image2.resize((370,230), Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(self.image2)
        self.new2 = Label(root,image=self.photo2,relief=SOLID,borderwidth=2)
        self.new2.place(x=1150,y=180)

        word_lable=Label(root,text="W_orldwide S_upply",font=('Microsoft Sans Serif',22,'bold'),bg="white",fg="black",bd=3)
        word_lable.place(x=1200,y=420)

        save_button = Button(root, text="Save", command=self.add_data,font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2")
        save_button.place(x=270, y=465, width=130, height=40)
        save_button.bind('<Return>', self.add_data)
        save_button.bind('<Button-1>', self.add_data)

        update_button = Button(root, text="Update", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                     fg="white", command=self.update,cursor="hand2")
        update_button.place(x=450, y=465, width=130, height=40)

        update_button.bind('<Return>',self.update)
        update_button.bind('<Button-1>', self.update)

        delete_button = Button(root, text="Delete", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                       fg="white", command=self.delete,cursor="hand2")
        delete_button.place(x=630, y=465, width=130, height=40)
        delete_button.bind('<Return>', self.delete)
        delete_button.bind('<Button-1>', self.delete)

        clear_button = Button(root, text="Clear", font=('goudy old style', 20, 'bold'), bg="#052320",
                                      fg="white", command=self.clear,cursor="hand2")
        clear_button.place(x=810, y=465, width=130, height=40)
        clear_button.bind('<Return>', self.clear)
        clear_button.bind('<Button-1>', self.clear)

        export=Button(root,text="Export_Data",font=('goudy old style',20,'bold'),bg="crimson",fg="white",borderwidth=3,command=self.export)
        export.place(x=990,y=465,height=40)
        export.bind('<Return>', self.export)
        export.bind('<Button-1>', self.export)




        rightmenu=Frame(root,relief=RIDGE,bd=2,bg="white")
        rightmenu.place(x=1390,y=520,width=140,height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")

        btn_employee=Button(rightmenu,text="Employee",image=self.right_arrow,compound=LEFT,command=self.employee1,padx=5,anchor="w",font=('times new roman',14,'bold'),bg="white",bd=3,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)


        btn_supplier = Button(rightmenu, text="Supplier", image=self.right_arrow,compound=LEFT, padx=5, command=self.supplier1,anchor="w",font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)


        btn_category = Button(rightmenu, text="Category", image=self.right_arrow,compound=LEFT,padx=5, anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3, command=self.category1,cursor="hand2")
        btn_category.pack(side=TOP, fill=X)


        btn_product = Button(rightmenu, text="Product",image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3,command=self.product1, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)


        btn_sales = Button(rightmenu, text="Sales", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                                     font=('times new roman', 14, 'bold'), bg="white", bd=3,command=self.sales1, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)


        btn_purchase = Button(rightmenu, text="Report", image=self.right_arrow,compound=LEFT, padx=5, anchor="w",
                                   font=('times new roman',14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.report1)
        btn_purchase.pack(side=TOP, fill=X)


        ims=Label(root,text="IMS",font=('times new roman',14,'bold'),fg="black",bg="white")
        ims.place(x=1480,y=770)

        r1 = Frame(root, bg="red")
        r1.place(x=1420, y=793, height=8, width=15)

        r2 = Frame(root, bg="orange")
        r2.place(x=1450, y=793, height=8, width=15)

        r3 = Frame(root, bg="#32cd32")
        r3.place(x=1480, y=793, height=8, width=15)

        r4 = Frame(root, bg="#00008b")
        r4.place(x=1510, y=793, height=8, width=15)



        data_show=Frame(root,bg="white",borderwidth=4,relief=SOLID)
        data_show.place(x=30,y=515,height=270,width=1350)

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style=ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15,'bold'))
        style.configure("Treeview",font=('times new roman', 12),anchor='CENTER')

        self.tabel = ttk.Treeview(data_show, columns=("Invoice_No", "Supplier_Name", "GST_Number", "Contact_No", "Supply_Product", "Price", "qty","Other_Information"),
                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel.xview)
        scroll_y.config(command=self.tabel.yview)


        self.tabel.heading("Invoice_No", text="Invoice_No")
        self.tabel.heading("Supplier_Name", text="Supplier_Name")
        self.tabel.heading("GST_Number", text="GST_Number")
        self.tabel.heading("Contact_No", text="Contact_No")
        self.tabel.heading("Supply_Product", text="Supply_Product")
        self.tabel.heading("Price", text="Price")
        self.tabel.heading("qty", text="qty")
        self.tabel.heading("Other_Information", text="Other_Information")
        self.tabel['show'] = 'headings'


        self.tabel.column("Invoice_No", width=220)
        self.tabel.column("Supplier_Name", width=220)
        self.tabel.column("GST_Number", width=220)
        self.tabel.column("Contact_No", width=220)
        self.tabel.column("Supply_Product", width=180)
        self.tabel.column("Price", width=180)
        self.tabel.column("qty", width=220)
        self.tabel.column("Other_Information", width=220)
        self.tabel.pack(fill=BOTH, expand=1)
        self.tabel.bind("<ButtonRelease-1>",self.get_data)
        self.fetch()

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

    def search_data(self,event):
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from supplier where " + str(self.var_search_by.get()) + " LIKE '%" + str(
                self.var_search_text.get()) + "%'")
            self.cmb_search.current(0)
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

    def export(self,event):
        file = filedialog.asksaveasfilename()
        get = self.tabel.get_children()
        first, second, third, four, fifth, six, seven, eight = [], [], [], [], [], [], [], []
        for i in get:
            content = self.tabel.item(i)
            val = content['values']
            first.append(val[0]), second.append(val[1]), third.append(val[2]), four.append(val[3]), fifth.append(
                val[4]), six.append(val[5]),
            seven.append(val[6]), eight.append(val[7])
        dd = ['Invoice_No', 'Supplier_Name', 'GST_Number', 'Contact_No', 'Supply_Product', 'Price', 'qty',
              'Other_Information']
        df = pandas.DataFrame(list(zip(first, second, third, four, fifth, six, seven, eight)), columns=dd)
        paths = r'{}.csv'.format(file)
        df.to_csv(paths, index=False)
        messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

    def delete(self,event):
        if (self.entry_invoice_no.get() == ""):
            messagebox.showerror("Delete", "Delete Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("delete from supplier where invoice_no='" + self.entry_invoice_no.get() + "'")
            cursor.execute("commit")

            self.entry_invoice_no.delete(0, 'end')
            self.entry_supplier_name.delete(0, 'end')
            self. entry_gst_number.delete(0, 'end')
            self.entry_contact_no.delete(0, 'end')
            self.entry_supply_product.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_other_information.delete(0, 'end')
            self.fetch()
            messagebox.showinfo("Delete Status", "Delete SucessFully")
            con.close()

    def update(self,event):
            invoice_no = self.entry_invoice_no.get()
            supplier_name = self.entry_supplier_name.get()
            gst_number = self.entry_gst_number.get()
            contact_no = self.entry_contact_no.get()
            supply_product = self.entry_supply_product.get()
            price = self.entry_price.get()
            qty = self.entry_qty.get()
            other_information = self.entry_other_information.get()

            if (
                    invoice_no == "" or supplier_name == "" or gst_number == "" or supply_product == "" or price == "" or qty == "" or other_information == ""):
                messagebox.showerror("Update Status", "All Flieds Are Requried")

            elif len(gst_number) < 16:
                messagebox.showerror("Error", "GST Number Should Be 16 Character")
            elif len(gst_number) > 16:
                messagebox.showerror("Error", "GST Number Only 16 Character")
            elif len(contact_no) < 10:
                messagebox.showerror("Error", "Contact Number Should Be 10 Character")
            elif len(contact_no) > 10:
                messagebox.showerror("Error", "Contact Number Only 10 Character")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                cursor.execute(
                    "update supplier set supplier_name='" + supplier_name + "',gst_number='" + gst_number + "',contact_no='" + contact_no + "',supply_product='" + supply_product + "',price='" + price + "',qty ='" + qty + "',other_information='" + other_information + "' where invoice_no='" + invoice_no + "'")
                cursor.execute("commit")
                self.entry_invoice_no.delete(0, 'end')
                self.entry_supplier_name.delete(0, 'end')
                self.entry_gst_number.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.entry_supply_product.delete(0, 'end')
                self.entry_price.delete(0, 'end')
                self.entry_qty.delete(0, 'end')
                self.entry_other_information.delete(0, 'end')
                self.fetch()
                messagebox.showinfo("Update Status", "Updated SucessFully")
                con.close()

    def clear(self,event):
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                cursor.execute("commit")
                self.entry_invoice_no.delete(0, 'end')
                self.entry_supplier_name.delete(0, 'end')
                self.entry_gst_number.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.entry_supply_product.delete(0, 'end')
                self.entry_price.delete(0, 'end')
                self.entry_qty.delete(0, 'end')
                self.entry_other_information.delete(0, 'end')
                self.txt_search.delete(0, 'end')
                self.cmb_search.current(0)
                messagebox.showinfo("Inform","Data will be clear")
                con.close()

    def get_data(self,event):
        cur = self.tabel.focus()
        left = self.tabel.item(cur)
        row = left['values']

        self.invoice_no.set(row[0])
        self.supplier_name.set(row[1])
        self.gst_number.set(row[2])
        self.contact_no.set(row[3])
        self.supply_product.set(row[4])
        self.price.set(row[5])
        self.qty.set(row[6])
        self.other_information.set(row[7])

    def checkcontact(self, con):
        if con.isdigit():
            return True
        if len(str(con)) == 0:
            return True


        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False

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
            cursor.execute("select *from supplier")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()

            con.close()

    def all_show(self,event):
            global rows
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from supplier")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()
            con.close()
            messagebox.showinfo("info", "All data in the display")

    def add_data(self,event):
        global rows
        invoice_no = self.entry_invoice_no.get()
        supplier_name = self.entry_supplier_name.get()
        gst_number = self.entry_gst_number.get()
        contact_no = self.entry_contact_no.get()
        supply_product = self.entry_supply_product.get()
        price = self.entry_price.get()
        qty = self.entry_qty.get()
        other_information = self.entry_other_information.get()

        if (
                invoice_no == "" or supplier_name == "" or gst_number == "" or contact_no == "" or supply_product == "" or price == "" or qty == "" or other_information == ""):
            messagebox.showerror("Insert Status", "ALL FILEDS ARE REQUIRED")
        elif len(gst_number) < 16:
            messagebox.showerror("Error", "GST Number Should Be 16 Character")
        elif len(gst_number) > 16:
            messagebox.showerror("Error", "GST Number Only 16 Character")
        elif len(contact_no) < 10:
            messagebox.showerror("Error", "Contact Number Should Be 10 Character")
        elif len(contact_no) > 10:
            messagebox.showerror("Error", "Contact Number Only 10 Character")
        else:

            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute(
                'INSERT INTO supplier( invoice_no , supplier_name, gst_number, contact_no ,supply_product, price, qty ,other_information )VALUES (%s, %s, %s,%s, %s, %s,%s, %s)',
                (invoice_no, supplier_name, gst_number, contact_no, supply_product, price, qty, other_information))
            cursor.execute("commit")
            self.entry_invoice_no.delete(0, 'end')
            self.entry_supplier_name.delete(0, 'end')
            self.entry_gst_number.delete(0, 'end')
            self.entry_contact_no.delete(0, 'end')
            self.entry_supply_product.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_other_information.delete(0, 'end')

            self.fetch()
            messagebox.showinfo("Insert Status", "Insert SucessFUlly")
            con.close()


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
        if c1 < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = supplierclass(self.new_window)  # employee file objet create  and import the file
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
    obj=supplierclass(root)
    root.mainloop()