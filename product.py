#librarey import
from tkinter import  *
from PIL import Image,ImageTk
from tkcalendar import  *
from tkinter import  ttk
from  tkcalendar import DateEntry
from tkinter import  messagebox ,filedialog
import mysql.connector as mysql
import  pandas
import tkinter.font
from tkinter.font import nametofont
import os

import employee
import  supplier
import  sales
import  category
import  dashoard
import reports







class productclass:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()  # fouce evenet used to focus on the screen


        root.state('zoomed')
        root.config(bg="white")

        root.title("Inventory Management System | Developed By Pritesh Bhatiya")

        root.focus_force()

        seacrhframe=LabelFrame(root,text="Search Category",bg="white",font=('goudy old style',16,'bold'),bd=2,relief=RIDGE)
        seacrhframe.place(x=50,y=25,width=950,height=90)
        self.var_search_by=StringVar()
        self.cmb_search=ttk.Combobox(seacrhframe,values=("Select","p_id","category_type"),state='readonly',textvariable=self.var_search_by,justify=CENTER,font=('times new roman',16))   #create combo box
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

        self.image1=Image.open('images/cat.jpg')
        self.image1=self.image1.resize((280,150), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(self.image1)
        self.new1 = Label(root,image=self.photo1,relief=SOLID,borderwidth=4)
        self.new1.place(x=1100)


        dashbboard_button = Button(root, text="Dashboard", font=('goudy old style', 16, 'bold'), bg="#052320",
                                    fg="white",cursor="hand2",command=self.dashboard1)
        dashbboard_button.place(x=1400,y=40, width=120, height=35)
        dashbboard_button.bind('<Return>', self.dashboard1)
        dashbboard_button.bind('<Button-1>', self.dashboard1)

        title=Label(root,text="Manage Product Details",font=('goudy old style',20,'bold'),bg="#0f4d7d",fg="white")
        title.place(x=0,y=130,relwidth=1)


        #1
        self.p_id =Label(root,text="Product_Id.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.p_id.place(x=40,y=190)
        self.p_id =StringVar()
        self.p_id.set("P_id")
        self.entry_p_id  =Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.p_id)
        self.entry_p_id .place(x=270,y=195,width=240,height=30)

        #2
        self.category_type = Label(root, text="Category_Type.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.category_type.place(x=570, y=190)
        self.category_type=StringVar()
        self.entry_category_type = Entry(root, font=('times new roman', 16), bg="lightyellow",
                                        textvariable=self.category_type)
        self.entry_category_type.place(x=800, y=195, width=240, height=30)




        #4
        self.product_name=Label(root,text="Product_Name.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.product_name.place(x=40,y=250)
        self.product_name=StringVar()
        self.entry_product_name=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.product_name)
        self.entry_product_name.place(x=270,y=255,width=240,height=30)

        #5
        self.price=Label(root,text="Price.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.price.place(x=570,y=250)
        self.price=StringVar()
        self.entry_price=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.price)
        self.entry_price.place(x=800,y=255,width=240,height=30)
        validate_price = root.register(self.checkprice)  # validation register
        self.entry_price.config(validate="key", validatecommand=(validate_price, "%P"))


        self.qty =Label(root,text="QTY.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.qty.place(x=40,y=310)
        self.qty=StringVar()
        self.entry_qty  =Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.qty)
        self.entry_qty .place(x=270,y=315,width=240,height=30)
        validate_qty = root.register(self.checkqty)  # validation register
        self.entry_qty.config(validate="key", validatecommand=(validate_qty, "%P"))

        self.amount=Label(root,text="Amount.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.amount.place(x=570,y=310)
        self.amount=StringVar()
        self.entry_amount=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.amount)
        self.entry_amount.place(x=800,y=315,width=240,height=30)


        self.status = Label(root, text="Status.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.status.place(x=40,y=370)
        self.status=StringVar()
        self.cmb_status=ttk.Combobox(root,values=("Select","Active","In Active"),state='readonly',textvariable=self.status,justify=CENTER,font=('times new roman',16))   #create combo box
        self.cmb_status.place(x=270,y=375,width=240,height=30)
        self.cmb_status.current(0)

        calculate = Button(root, text="Calculate", command=self.calc,font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                       fg="white", cursor="hand2")
        calculate.place(x=680, y=355, width=130, height=40)
        calculate.bind('<Return>', self.calc)
        calculate.bind('<Button-1>', self.calc)

        cat1=Frame(root, relief=RIDGE, bd=2, bg="white")
        cat1.place(x=1100,y=185,height=280,width=400)
        data_show = Frame(cat1, bg="white", borderwidth=2, relief=RIDGE)
        data_show.place(height=274, relwidth=1,)

        scroll_x = x = Scrollbar(data_show, orient=HORIZONTAL)
        scroll_y = y = Scrollbar(data_show, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel_2 = ttk.Treeview(data_show,
                                    columns=(
                                        "Category_Type", "Category_Name"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel_2.xview)
        scroll_y.config(command=self.tabel_2.yview)


        self.tabel_2.heading("Category_Type", text="Category_Type")
        self.tabel_2.heading("Category_Name", text="Category_Name")

        self.tabel_2['show'] = 'headings'


        self.tabel_2.column("Category_Type", width=180)
        self.tabel_2.column("Category_Name", width=200)

        self.tabel_2.pack(fill=BOTH, expand=1)
        self.tabel_2.bind("<ButtonRelease-1>", self.get_data1)
        self.fetch_2()




        word_lable=Label(root,text="W_orldwide S_upply",font=('Microsoft Sans Serif',22,'bold'),bg="white",fg="black",bd=3)
        word_lable.place(x=1200,y=470)

        save_button = Button(root, text="Add", command=self.add_data,font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2")
        save_button.place(x=250, y=440, width=130, height=40)
        save_button.bind('<Return>', self.add_data)
        save_button.bind('<Button-1>', self.add_data)

        update_button = Button(root, text="Update", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                     fg="white", command=self.update,cursor="hand2")
        update_button.place(x=430, y=440, width=130, height=40)
        update_button.bind('<Return>', self.update)
        update_button.bind('<Button-1>', self.update)

        delete_button = Button(root, text="Delete", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                       fg="white", command=self.delete,cursor="hand2")
        delete_button.place(x=610, y=440, width=130, height=40)
        delete_button.bind('<Return>', self.delete)
        delete_button.bind('<Button-1>', self.delete)

        clear_button = Button(root, text="Clear", font=('goudy old style', 20, 'bold'), bg="#052320",
                                      fg="white", command=self.clear,cursor="hand2")
        clear_button.place(x=790, y=440, width=130, height=40)
        clear_button.bind('<Return>', self.clear)
        clear_button.bind('<Button-1>', self.clear)

        rightmenu=Frame(root,relief=RIDGE,bd=2,bg="white")
        rightmenu.place(x=1390,y=520,width=140,height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")

        btn_employee=Button(rightmenu,text="Employee",image=self.right_arrow,compound=LEFT,padx=5,command=self.employee1,anchor="w",font=('times new roman',14,'bold'),bg="white",bd=3,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)

        btn_supplier = Button(rightmenu, text="Supplier", image=self.right_arrow,compound=LEFT, padx=5, command=self.supplier1,anchor="w",font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)


        btn_category = Button(rightmenu, text="Category", image=self.right_arrow,compound=LEFT,padx=5,command=self.category1, anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)


        btn_product = Button(rightmenu, text="Product",image=self.right_arrow, compound=LEFT, padx=5,anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.product1)
        btn_product.pack(side=TOP, fill=X)


        btn_sales = Button(rightmenu, text="Sales", image=self.right_arrow, compound=LEFT, padx=5, anchor="w",
                                     font=('times new roman', 14, 'bold'), bg="white", bd=3, command=self.sales1,cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)

        btn_report = Button(rightmenu, text="Report", image=self.right_arrow,compound=LEFT, padx=5, anchor="w",
                                   font=('times new roman',14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.report1)
        btn_report.pack(side=TOP, fill=X)


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

        self.tabel = ttk.Treeview(data_show, columns=("P_id", "Category_Type", "Product_Name", "Price","QTY","Amount","Status"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel.xview)
        scroll_y.config(command=self.tabel.yview)


        self.tabel.heading("P_id", text="P_id")
        self.tabel.heading("Category_Type", text="Category_Type")
        self.tabel.heading("Product_Name", text="Product_Name")
        self. tabel.heading("Price", text="Price")
        self.tabel.heading("QTY",text="QTY")
        self.tabel.heading("Amount",text="Amount")
        self.tabel.heading("Status",text="Status")
        self.tabel['show'] = 'headings'


        self.tabel.column("P_id", width=220)
        self.tabel.column("Category_Type", width=220)
        self.tabel.column("Product_Name", width=220)
        self.tabel.column("Price", width=220)
        self.tabel.column("QTY", width=220)
        self.tabel.column("Amount", width=220)
        self.tabel.column("Status", width=220)
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

    def  calc(self,event):
        self.amount.set(int(self.price.get()) * int(self.qty.get()))

    def add_data(self,event):
        global rows


        category_type = self.entry_category_type.get()
        product_name = self.entry_product_name.get()
        price = self.entry_price.get()
        qty = self.entry_qty.get()
        amount = self.entry_amount.get()
        status = self.cmb_status.get()

        if (
         category_type == "" or product_name == "" or price == "" or qty == "" or amount == "" or status == ""):
            messagebox.showerror("Insert Status", "ALL FILEDS ARE REQUIRED")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            # cursor.execute("insert into employee values('" + emp_id + "','" + gender + "','" + contact_no + "','" + name + "','" + dob + "','" + doj + "','" + email + "','" + password + "','" + user_type + "','" + address + "'," + salary + "')")
            cursor.execute(
                'INSERT INTO product(category_type, product_name, price,qty,amount,status )VALUES ( %s, %s,%s,%s,%s,%s)',
                (category_type, product_name, price, qty, amount, status))
            cursor.execute("commit")
            self.p_id.set("P_id")
            self.entry_p_id.delete(0, 'end')
            self.entry_category_type.delete(0,'end')
            self.entry_product_name.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_amount.delete(0, 'end')
            self.cmb_status.current(0)
            self.fetch()
            messagebox.showinfo("Insert Status", "Insert SucessFUlly")
            con.close()

    def fetch(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from product")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', END, values=row)
                con.commit()

        con.close()
    def fetch_2(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select category_type,category_name from category")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel_2.delete(*self.tabel_2.get_children())
            for row in rows:
                self.tabel_2.insert('', END, values=row)
                con.commit()

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

    def all_show(self,event):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from product")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', END, values=row)
                con.commit()

        con.close()
        messagebox.showinfo("info", "All data in the display")

    def get_data(self,event):
        cur = self.tabel.focus()
        left = self.tabel.item(cur)
        row = left['values']

        self.p_id.set(row[0])
        self.category_type.set(row[1])
        self.product_name.set(row[2])
        self.price.set(row[3])
        self.qty.set(row[4])
        self.amount.set(row[5])
        self.status.set(row[6])

    def get_data1(self,event):
            cur = self.tabel_2.focus()
            left = self.tabel_2.item(cur)
            row = left['values']

            self.category_type.set(row[0])
            self.product_name.set(row[1])

    def clear(self,event):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("commit")
        self.p_id.set("P_id")
        self.entry_category_type.delete(0,'end')
        self.entry_product_name.delete(0, 'end')
        self.entry_price.delete(0, 'end')
        self.entry_qty.delete(0, 'end')
        self.entry_amount.delete(0, 'end')
        self.cmb_status.current(0)
        self.cmb_search.current(0)
        messagebox.showinfo("Inform", "Data will be clear")
        con.close()

    def update(self,event):
        p_id = self.entry_p_id.get()
        category_type = self.entry_category_type.get()
        product_name = self.entry_product_name.get()
        price = self.entry_price.get()
        qty = self.entry_qty.get()
        amount = self.entry_amount.get()
        status = self.cmb_status.get()

        if (
                p_id == "" or category_type == "" or product_name == "" or price == "" or qty == "" or amount == "" or status == ""):
            messagebox.showerror("Update Status", "All Flieds Are Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute(
                "update product set category_type='" + category_type + "', product_name ='" + product_name + "',price='" + price + "', qty='" + qty + "',amount='" + amount + "',status='" + status + "' where  p_id='" + p_id + "'")
            cursor.execute("commit")
            self.p_id.set("P_id")
            self.entry_category_type.delete(0,'end')
            self.entry_product_name.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_amount.delete(0, 'end')
            self.cmb_status.current(0)
            self.fetch()
            messagebox.showinfo("Update Status", "Updated SucessFully")
            con.close()

    def delete(self,event):
        if (self.entry_p_id.get() == ""):
            messagebox.showerror("Delete", "Delete Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("delete from product where p_id='" + self.entry_p_id.get() + "'")
            cursor.execute("commit")

            self.p_id.set("P_id")
            self.entry_category_type.delete(0,'end')
            self.entry_product_name.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_amount.delete(0, 'end')
            self.cmb_status.current(0)
            self.fetch()
            messagebox.showinfo("Delete Status", "Delete SucessFully")
            con.close()

    def search_data(self,event):

        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute(
            "select *from product where " + str(self.var_search_by.get()) + " LIKE '%" + str(self.var_search_text.get()) + "%'")
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

    def employee1(self):
        global counter
        if counter < 2:
            self.root.destroy()
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = employee.employeeclass(self.new_window)  # employee file objet create  and import the file
            counter += 1

        else:
            messagebox.showinfo("Error", "Hey! You've already opened a employee window!")

    def supplier1(self):
        global c1
        if c1 < 2:
            self.old_window = Toplevel(self.root)
            self.new_obj = supplier.supplierclass(self.old_window)  # employee file objet create  and import the file
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
        if c3 < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = productclass(self.new_window)  # employee file objet create  and import the file
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
    obj=productclass(root)
    root.mainloop()