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



import  employee
import  supplier
import  product
import  sales
import  dashoard
import reports



class categoryclass:
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
        self.cmb_search=ttk.Combobox(seacrhframe,values=("Select","c_id","category_type"),state='readonly',textvariable=self.var_search_by,justify=CENTER,font=('times new roman',16))   #create combo box
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


        title=Label(root,text="Manage Product Category",font=('goudy old style',20,'bold'),bg="#0f4d7d",fg="white")
        title.place(x=0,y=130,relwidth=1)


        #1
        self.c_id =Label(root,text="Category_Id.",fg="black",font=('goudy old styl=',18,'bold'),bg="white")
        self.c_id.place(x=40,y=190)
        self.c_id =StringVar()
        self.c_id.set("C_id")
        self.entry_c_id  =Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.c_id )
        self.entry_c_id  .place(x=270,y=195,width=240,height=30)

        #2
        self.category_type = Label(root, text="Category_Type.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.category_type.place(x=570, y=190)
        self.category_type=StringVar()
        self.cmb_category_type=ttk.Combobox(root,values=("Select","Marine Exports","Industrial Supplies"),state='readonly',textvariable=self.category_type,justify=CENTER,font=('times new roman',16))   #create combo box
        self.cmb_category_type.place(x=800,y=195,width=240,height=30)
        self.cmb_category_type.current(0)




        #4
        self.category_name=Label(root,text="Category_Name.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.category_name.place(x=40,y=250)
        self.category_name=StringVar()
        self.entry_category_name=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.category_name)
        self.entry_category_name.place(x=270,y=255,width=240,height=30)

        #5
        self.category_code=Label(root,text="Category_Code.",fg="black",bg="white",font=('goudy old style',18,'bold'))
        self.category_code.place(x=570,y=250)
        self.category_code=StringVar()
        self.entry_category_code=Entry(root,font=('times new roman',16),bg="lightyellow",textvariable=self.category_code)
        self.entry_category_code.place(x=800,y=255,width=240,height=30)



        self.image2=Image.open('images/supply.jpg')
        self.image2=self.image2.resize((370,230), Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(self.image2)
        self.new2 = Label(root,image=self.photo2,relief=SOLID,borderwidth=2)
        self.new2.place(x=1150,y=180)

        word_lable=Label(root,text="W_orldwide S_upply",font=('Microsoft Sans Serif',22,'bold'),bg="white",fg="black",bd=3)
        word_lable.place(x=1200,y=420)

        save_button = Button(root, text="Add", command=self.add_data,font=('goudy old style', 20, 'bold'), bg="#020063",
                                       fg="white", cursor="hand2")
        save_button.place(x=250, y=310, width=130, height=40)
        save_button.bind('<Return>', self.add_data)
        save_button.bind('<Button-1>', self.add_data)

        update_button = Button(root, text="Update", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                                     fg="white", command=self.update,cursor="hand2")
        update_button.place(x=430, y=310, width=130, height=40)
        update_button.bind('<Return>', self.update)
        update_button.bind('<Button-1>', self.update)

        delete_button = Button(root, text="Delete", font=('goudy old style', 20, 'bold'), bg="#db0909",
                                       fg="white", command=self.delete,cursor="hand2")
        delete_button.place(x=610, y=310, width=130, height=40)
        delete_button.bind('<Return>', self.delete)
        delete_button.bind('<Button-1>', self.delete)

        clear_button = Button(root, text="Clear", font=('goudy old style', 20, 'bold'), bg="#052320",
                                      fg="white", command=self.clear,cursor="hand2")
        clear_button.place(x=790, y=310, width=130, height=40)
        clear_button.bind('<Return>', self.clear)
        clear_button.bind('<Button-1>', self.clear)


        self.image3=Image.open('images/export.jpg')
        self.image3=self.image3.resize((370,140), Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(self.image3)
        self.new3 = Label(root,image=self.photo3,bg="white",fg="black",relief=SOLID,borderwidth=3)
        self.new3.place(x=15,y=360)

        d1=Label(root,text="Marine_Export",font=('Microsoft Sans Serif',22,'bold'),bg="white",fg="black",bd=3)
        d1.place(x=400,y=400)

        d2= Label(root, text="Industrial_Supplies", font=('Microsoft Sans Serif', 22, 'bold'), bg="white", fg="black", bd=3)
        d2.place(x=470, y=450)









        self.image6=Image.open('images/trucklocatio.jpg')
        self.image6=self.image6.resize((370,140), Image.ANTIALIAS)
        self.photo6=ImageTk.PhotoImage(self.image6)
        self.new6 = Label(root,image=self.photo6,bg="white",fg="black",relief=SOLID,borderwidth=3)
        self.new6.place(x=750,y=360)



        rightmenu=Frame(root,relief=RIDGE,bd=2,bg="white")
        rightmenu.place(x=1390,y=520,width=140,height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")

        btn_employee=Button(rightmenu,text="Employee",image=self.right_arrow,compound=LEFT,padx=5,anchor="w",command=self.employee1,font=('times new roman',14,'bold'),bg="white",bd=3,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)


        btn_supplier = Button(rightmenu, text="Supplier", image=self.right_arrow,compound=LEFT,  padx=5, command=self.supplier1,anchor="w",font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)


        btn_category = Button(rightmenu, text="Category", image=self.right_arrow,compound=LEFT,padx=5, command=self.category1,anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)


        btn_product = Button(rightmenu, text="Product",image=self.right_arrow, compound=LEFT,padx=5, command=self.product1,anchor="w",
                                      font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)

        btn_sales = Button(rightmenu, text="Sales", image=self.right_arrow, compound=LEFT,padx=5, command=self.sales1,anchor="w",
                                     font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
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

        self.tabel = ttk.Treeview(data_show, columns=("C_id", "Category_Type", "Category_Name", "Category_Code"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.tabel.xview)
        scroll_y.config(command=self.tabel.yview)


        self.tabel.heading("C_id", text="C_id")
        self.tabel.heading("Category_Type", text="Category_Type")
        self.tabel.heading("Category_Name", text="Category_Name")
        self.tabel.heading("Category_Code", text="Category_Code")
        self.tabel['show'] = 'headings'


        self.tabel.column("C_id", width=220)
        self.tabel.column("Category_Type", width=220)
        self.tabel.column("Category_Name", width=220)
        self.tabel.column("Category_Code", width=220)
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
        c6= 1

    def search_data(self,event):

            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("select *from category where " + str(self.var_search_by.get()) + " LIKE '%" + str(
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

    def add_data(self,event):
        global rows


        category_type = self.cmb_category_type.get()
        category_name = self.entry_category_name.get()
        category_code = self.entry_category_code.get()

        if (category_type == "" or category_name == "" or category_code == ""):
            messagebox.showerror("Insert Status", "ALL FILEDS ARE REQUIRED")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            # cursor.execute("insert into employee values('" + emp_id + "','" + gender + "','" + contact_no + "','" + name + "','" + dob + "','" + doj + "','" + email + "','" + password + "','" + user_type + "','" + address + "'," + salary + "')")
            cursor.execute(
                'INSERT INTO category(category_type, category_name, category_code )VALUES (%s, %s,%s)',
                (category_type, category_name, category_code))
            cursor.execute("commit")
            self.c_id.set("C_id")
            self.cmb_category_type.current(0)
            self.entry_category_name.delete(0, 'end')
            self.entry_category_code.delete(0, 'end')
            self.fetch()
            messagebox.showinfo("Insert Status", "Insert SucessFUlly")
            con.close()

    def fetch(self):
        global rows
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("select *from category")
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
        cursor.execute("select *from category")
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

        self.c_id.set(row[0])
        self.category_type.set(row[1])
        self.category_name.set(row[2])
        self.category_code.set(row[3])

    def clear(self,event):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("commit")
        self.c_id.set("C_id")
        self.cmb_category_type.current(0)
        self.entry_category_name.delete(0, 'end')
        self.entry_category_code.delete(0, 'end')
        self.txt_search.delete(0, 'end')
        self.cmb_search.current(0)
        messagebox.showinfo("Inform", "Data will be clear")
        con.close()

    def update(self,event):
        c_id = self.entry_c_id.get()
        category_type = self.cmb_category_type.get()
        category_name = self.entry_category_name.get()
        category_code = self.entry_category_code.get()

        if (c_id == "" or category_type == "" or category_name == "" or category_code == ""):
            messagebox.showerror("Update Status", "All Flieds Are Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute(
                "update category set category_type='" + category_type + "',category_name='" + category_name + "',category_code='" + category_code + "' where  c_id='" + c_id + "'")
            cursor.execute("commit")
            self.c_id.set("C_id")
            self.cmb_category_type.current(0)
            self.entry_category_name.delete(0, 'end')
            self.entry_category_code.delete(0, 'end')
            self.fetch()
            messagebox.showinfo("Update Status", "Updated SucessFully")
            con.close()

    def delete(self,event):
        if (self.entry_c_id.get() == ""):
            messagebox.showerror("Delete", "Delete Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("delete from category where c_id='" + self.entry_c_id.get() + "'")
            cursor.execute("commit")

            self.c_id.set("C_id")
            self.cmb_category_type.current(0)
            self.entry_category_name.delete(0, 'end')
            self.entry_category_code.delete(0, 'end')
            self.fetch()
            messagebox.showinfo("Delete Status", "Delete SucessFully")
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
        try:
            global c1
            if c1 < 2:
                self.new_window = Toplevel(self.root)  # creat top leveal
                self.new_obj = supplier.supplierclass(self.new_window)  # employee file objet create  and import the file
                c1 += 1
            else:
                messagebox.showinfo("Error", "Hey! You've already opened a suplier window!")
        except Exception as e:
                messagebox.showinfo("error")

    def category1(self):
        global c2
        if c2 < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = categoryclass(self.new_window)  # employee file objet create  and import the file
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
    obj=categoryclass(root)
    root.mainloop()

