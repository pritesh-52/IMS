#librarey import
from tkinter import  *
from PIL import Image,ImageTk
from tkcalendar import  *
from tkinter import  ttk
from  tkcalendar import DateEntry
from tkinter import  messagebox ,filedialog
import mysql.connector as mysql
import pandas
import  supplier
import  category
import  product
import  sales
import  dashoard
import reports
import re
import os
import sys
import  tracestack



class employeeclass:    #main class of the gui windows defined

    def __init__(self,root):   #constrtuort is used for create tkinter object


        self.root=root
        self.root.state('zoomed')
        self.root.config(bg="white")


        self.root.title("Inventory Management System | Developed By Pritesh Bhatiya")

        self.root.focus_force()

        self.seacrhframe = LabelFrame(self.root, text="Search Employee", bg="white", font=('goudy old style', 16, 'bold'), bd=2,
                                 relief=RIDGE)
        self.seacrhframe.place(x=50, y=25, width=950, height=90)
        self.var_search_by = StringVar()
        self.cmb_search = ttk.Combobox(self.seacrhframe, values=("Select", "emp_id", "name", "email"), state='readonly',
                                  textvariable=self.var_search_by, justify=CENTER,
                                  font=('times new roman', 16))  # create combo box
        self.cmb_search.place(x=30, y=15, width=200)
        self.cmb_search.current(0)

        self.var_search_text = StringVar()
        self.txt_search = Entry(self.seacrhframe, textvariable=self.var_search_text, font=('goudy old style', 15), bg="lightyellow")
        self.txt_search.place(x=270, y=15, width=250, height=30)

        self.search_button = Button(self.seacrhframe, text="Search", font=('goudy old style', 18, 'bold'), bg="#4caf50",
                               fg="white", cursor="hand2",command=self.search_data)
        self.search_button.place(x=550, y=15, width=180, height=35)

        self.search_button.bind('<Return>',self.search_data)

        self.search_button.bind('<ButtonRelease-1>', self.search_data)


        self.showall_button = Button(self.seacrhframe, text="Show All", font=('goudy old style', 18, 'bold'), bg="#4caf50",
                                fg="white", cursor="hand2",command=self.fetch)
        self.showall_button.place(x=750, y=15, width=180, height=35)

        self.showall_button.bind('<Return>', self.all_show)

        self.showall_button.bind('<ButtonRelease-1>', self.all_show)




        self.image1 = Image.open('images/emp.jpg')
        self.image1 = self.image1.resize((280, 150), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.new1 = Label(root, image=self.photo1, relief=SOLID, borderwidth=4)
        self.new1.place(x=1100)

        self.dashbboard_button = Button(self.root, text="Dashboard", font=('goudy old style', 16, 'bold'), bg="#052320",
                                    fg="white", command=self.dashboard1,cursor="hand2")
        self.dashbboard_button.place(x=1400, y=40, width=120, height=35)
        self.dashbboard_button.bind('<Return>',self.dashboard1)
        self.dashbboard_button.bind('<Button-1>', self.dashboard1)

        self.title = Label(self.root, text="Employee Details", font=('goudy old style', 20, 'bold'), bg="#0f4d7d", fg="white")
        self.title.place(x=0, y=130, relwidth=1)

        # 1
        self.emp_id = Label(self.root, text="Emp No.", fg="black", font=('goudy old styl=', 18, 'bold'), bg="white")
        self.emp_id.place(x=40, y=190)
        self.emp_id = StringVar()
        self.emp_id.set("Emp No")
        self.entry_emp_id = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.emp_id)
        self.entry_emp_id.place(x=180, y=195, width=240, height=30)

        # 2
        self.gender = Label(self.root, text="Gender.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.gender.place(x=520, y=190)
        self.gender = StringVar()
        self.cmb_gender = ttk.Combobox(self.root, values=("Select", "Male", "Female", "Other"), state='readonly',
                                  textvariable=self.gender, justify=CENTER, font=('times new roman', 16))  # create combo box
        self.cmb_gender.place(x=670, y=195, width=240, height=30)
        self.cmb_gender.current(0)

        # 3
        self.contact_no = Label(self.root, text="Contact No.", fg="black", font=('goudy old style', 18, 'bold'), bg="white")
        self.contact_no.place(x=960, y=190)
        self.contact_no = StringVar()
        self.entry_contact_no = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.contact_no)
        self.entry_contact_no.place(x=1150, y=195, width=240, height=30)
        validate_contact = root.register(self.checkcontact)  # validation register
        self.entry_contact_no.config(validate="key", validatecommand=(validate_contact, "%P"))

        # 4
        self.name = Label(self.root, text="Name.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.name.place(x=40, y=250)
        self.name = StringVar()
        self.entry_name = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.name)
        self.entry_name.place(x=180, y=255, width=240, height=30)

        # 5
        self.dob = Label(self.root, text="D.O.B.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.dob.place(x=520, y=250)
        self.dob = StringVar()
        self.entry_dob = DateEntry(self.root, font=('times new roman', 16), bg="lightyellow", selectmode='day', textvariable=self.dob)
        self.entry_dob.place(x=670, y=255, width=240, height=30)

        # 6
        self.doj = Label(self.root, text="D.O.J.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.doj.place(x=960, y=250)
        self.doj = StringVar()
        self.entry_doj = DateEntry(self.root, font=('times new roman', 16), bg="lightyellow", selectmode='day', textvariable=self.doj)
        self.entry_doj.place(x=1150, y=255, width=240, height=30)

        # 7
        self.email = Label(self.root, text="Email.", font=('goudy old style', 18, 'bold'), fg="black", bg="white")
        self.email.place(x=40, y=310)
        self. email = StringVar()
        self.entry_email = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.email)
        self.entry_email.place(x=180, y=315, width=240, height=30)

        # 8
        self.department = Label(self.root, text="Department.", font=('goudy old style', 18, 'bold'), fg="black", bg="white")
        self.department.place(x=520, y=310)
        self.department = StringVar()
        '''self.entry_department = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.department)
        self.entry_department.place(x=670, y=315, width=240, height=30)'''
        self.cmb_department = ttk.Combobox(self.root, values=("Select", "Accounting", "Purchase", "Sales","Production"), state='readonly',
                                       textvariable=self.department, justify=CENTER,
                                       font=('times new roman', 16))  # create combo box
        self.cmb_department.place(x=670, y=315, width=240, height=30)
        self.cmb_department.current(0)

        # 9
        self.usertype = Label(self.root, text="User Type.", font=('goudy old style', 18, 'bold'), fg="black", bg="white")
        self.usertype.place(x=960, y=310)
        self.user_type = StringVar(value='Employee')
        self.user_type_entry = Entry(self.root, font=('times new roman', 16), bg="lightyellow", state='readonly',
                                textvariable=self.user_type)
        self.user_type_entry.place(x=1150, y=315, width=240, height=30)


        # 10
        self.address = Label(self.root, text="Address.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.address.place(x=40, y=370)
        self.address = StringVar()
        self.entry_address = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.address)
        self.entry_address.place(x=180, y=375, width=330, height=80)

        # 11
        self.salary = Label(self.root, text="Salary.", fg="black", bg="white", font=('goudy old style', 18, 'bold'))
        self.salary.place(x=520, y=370)
        self.salary = StringVar()
        self.entry_salary = Entry(self.root, font=('times new roman', 16), bg="lightyellow", textvariable=self.salary)
        self.entry_salary.place(x=670, y=375, width=240, height=30)
        validate_salery = root.register(self.checkcsalary)  # validation register
        self.entry_salary.config(validate="key", validatecommand=(validate_salery, "%P"))

        self.image2 = Image.open('images/empworker.jpg')
        self.image2 = self.image2.resize((130, 180), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.new2 = Label(root, image=self.photo2)
        self.new2.place(x=1400,y=200)

        self.save_button = Button(self.root, text="Save",  font=('goudy old style', 20, 'bold'), bg="#020063",
                             fg="white", cursor="hand2",command=self.add_data)
        self.save_button.place(x=800, y=420, width=130, height=40)
        self.save_button.bind('<Return>',self.add_data)

        self.save_button.bind('<ButtonRelease-1>', self.add_data)




        self.update_button = Button(self.root, text="Update", font=('goudy old style', 20, 'bold'), bg="#0a5615",
                               fg="white",  cursor="hand2",command=self.update)
        self.update_button.place(x=950, y=420, width=130, height=40)

        self.update_button.bind('<Return>',self.update)

        self.update_button.bind('<ButtonRelease-1>', self.update)



        self.delete_button = Button(self.root, text="Delete", font=('goudy old style', 20, 'bold'), bg="#db0909",
                               fg="white",  cursor="hand2",command=self.delete)
        self.delete_button.place(x=1100, y=420, width=130, height=40)

        self.delete_button.bind('<Return>', self.delete)

        self.delete_button.bind('<ButtonRelease-1>', self.delete)





        self.clear_button = Button(self.root, text="Clear", font=('goudy old style', 20, 'bold'), bg="#052320",
                              fg="white",  cursor="hand2",command=self.clear_all)
        self.clear_button.place(x=1250, y=420, width=130, height=40)

        self.clear_button.bind('<Return>',self.clear_all)

        self.clear_button.bind('<ButtonRelease-1>',self.clear_all)



        self.export = Button(self.root, text="Export_Data", font=('goudy old style', 20, 'bold'), bg="crimson", fg="white",
                        borderwidth=3,command=self.export_1 )
        self.export.place(x=1330, y=468, height=40)

        self.export.bind('<Return>', self.export_1)

        self.export.bind('<ButtonRelease-1>', self.export_1)


        self.rightmenu = Frame(self.root, relief=RIDGE, bd=2, bg="white")
        self.rightmenu.place(x=1390, y=520, width=140, height=250)

        self.right_arrow = PhotoImage(file="images/icons.png")

        self.btn_employee = Button(self.rightmenu, text="Employee", image=self.right_arrow,compound=LEFT, padx=5,
                              anchor="w", font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.employee1)
        self.btn_employee.pack(side=TOP, fill=X)




        self.btn_supplier = Button(self.rightmenu, text="Supplier", image=self.right_arrow, command=self.supplier1, compound=LEFT,  padx=5,
                              anchor="w", font=('times new roman', 14, 'bold'),bg="white", bd=3, cursor="hand2")
        self.btn_supplier.pack(side=TOP, fill=X)



        self.btn_category = Button(self.rightmenu, text="Category", image=self.right_arrow, command=self.category1, compound=LEFT,  padx=5,
                              anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        self.btn_category.pack(side=TOP, fill=X)




        self.btn_product = Button(self.rightmenu, text="Product", image=self.right_arrow,  command=self.product1,compound=LEFT, padx=5,
                             anchor="w",
                             font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        self.btn_product.pack(side=TOP, fill=X)




        self.btn_sales = Button(self.rightmenu, text="Sales", image=self.right_arrow,  command=self.sales1,compound=LEFT,padx=5,
                           anchor="w",
                           font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2")
        self.btn_sales.pack(side=TOP, fill=X)


        self.btn_purchase = Button(self.rightmenu, text="Report", image=self.right_arrow, compound=LEFT, padx=5,
                              anchor="w",
                              font=('times new roman', 14, 'bold'), bg="white", bd=3, cursor="hand2",command=self.report1)
        self.btn_purchase.pack(side=TOP, fill=X)

        self.ims = Label(self.root, text="IMS", font=('times new roman', 14, 'bold'), fg="black", bg="white")
        self.ims.place(x=1480, y=770)

        self.r1 = Frame(self.root, bg="red")
        self.r1.place(x=1420, y=793, height=8, width=15)

        self.r2 = Frame(self.root, bg="orange")
        self.r2.place(x=1450, y=793, height=8, width=15)

        self.r3 = Frame(self.root, bg="#32cd32")
        self.r3.place(x=1480, y=793, height=8, width=15)

        self.r4 = Frame(self.root, bg="#00008b")
        self.r4.place(x=1510, y=793, height=8, width=15)

        self.data_show = Frame(self.root, bg="white", borderwidth=4, relief=SOLID)
        self.data_show.place(x=30, y=515, height=270, width=1350)

        self.scroll_x = x = Scrollbar(self.data_show, orient=HORIZONTAL)
        self.scroll_y = y = Scrollbar(self.data_show, orient=VERTICAL)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('times new roman', 15, 'bold'))
        self.style.configure("Treeview", font=('times new roman', 12), anchor='CENTER')

        self.tabel = ttk.Treeview(self.data_show, columns=(
        "Emp No", "Name", "Email", "Contact No", "Gender", "D.O.B", "D.O.J", "Salary", "Address", "Department",
        "User Type"),
                             xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.tabel.xview)
        self.scroll_y.config(command=self.tabel.yview)

        self.tabel.heading("Emp No", text="Emp No")
        self.tabel.heading("Name", text="Name")
        self.tabel.heading("Email", text="Email")
        self.tabel.heading("Contact No", text="Contact No")
        self.tabel.heading("Gender", text="Gender")
        self.tabel.heading("D.O.B", text="D.O.B")
        self.tabel.heading("D.O.J", text="D.O.J")
        self.tabel.heading("Salary", text="Salary")
        self.tabel.heading("Address", text="Address")
        self.tabel.heading("Department", text="Department")
        self.tabel.heading("User Type", text="User Type")
        self.tabel['show'] = 'headings'

        self.tabel.column("Emp No", width=180)
        self.tabel.column("Name", width=220)
        self.tabel.column("Email", width=220)
        self.tabel.column("Contact No", width=220)
        self.tabel.column("Gender", width=220)
        self.tabel.column("D.O.B", width=180)
        self.tabel.column("D.O.J", width=180)
        self.tabel.column("Salary", width=220)
        self.tabel.column("Address", width=220)
        self.tabel.column("Department", width=220)
        self.tabel.column("User Type", width=220)
        self.tabel.pack(fill=BOTH, expand=1)
        self.tabel.bind("<ButtonRelease-1>", self.get_data)
        self.fetch()

        self.root.bind('<Delete>', self.delete)
        self.root.bind("<Escape>", exit)



        global counter
        counter = 1

        global c1
        c1= 1

        global c2
        c2= 1

        global c3
        c3 = 1

        global c4
        c4 = 1

        global c5
        c5 = 1

        global c6
        c6 = 1


    def employee1(self):

        global counter
        if counter < 1:
            self.new_window = Toplevel(self.root)  # creat top leveal
            self.new_obj = employeeclass(self.new_window)  # employee file objet create  and import the file
            counter += 1
        else:
            messagebox.showinfo("Error", "Hey! You've already opened a employee window!")



    def supplier1(self):

        global c1

        if c1 < 2:
            self.old_window=Toplevel(self.root)
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

    def checkcontact(self,con):
        if con.isdigit():
            return True
        if len(str(con)) == 0:
            return True


        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False

    def checkcsalary(self, sal):
        if sal.isdigit():
            return True
        if len(str(sal)) == 0:
            return True
        else:
            messagebox.showwarning("Invalid", "Only Number Allowed")
            return False
    def checkemail(self,email):

        if len(email) > 7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
                return True
            else:
                messagebox.showwarning("Alert", "Invalid E-mail id ")
                return False
        else:
            messagebox.showwarning("Alert", "Email length is too small")

    def add_data(self,event):
        global rows
        x = 0

        name = self.entry_name.get()
        email = self.entry_email.get()
        contact_no = self.entry_contact_no.get()
        gender = self.cmb_gender.get()
        dob = self.entry_dob.get()
        doj = self.entry_doj.get()
        salary = self.entry_salary.get()
        address = self.entry_address.get()
        department = self.cmb_department.get()
        user_type = self.user_type_entry.get()

        if ( name == "" or email == "" or contact_no == "" or gender == "" or dob == "" or doj == "" or salary == "" or address == "" or department == "" or user_type == ""):
            messagebox.showinfo("Insert Status", "ALL FILEDS ARE REQUIRED")
        elif len(contact_no)<10:
            messagebox.showwarning("Alert","Contact Number Should Be 10 Character")
        elif len(contact_no)>10:
            messagebox.showwarning("Alert","Contact Number Only 10 Character")
        elif self.email.get() !=None:
            x=self.checkemail(self.email.get())
        if(x==True):

            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            # cursor.execute("insert into employee values('" + emp_id + "','" + gender + "','" + contact_no + "','" + name + "','" + dob + "','" + doj + "','" + email + "','" + password + "','" + user_type + "','" + address + "'," + salary + "')")
            cursor.execute(
                'INSERT INTO employee(name, email, contact_no ,gender, dob,doj,salary ,address,department ,user_type )VALUES (%s, %s,%s, %s, %s,%s, %s, %s,%s,%s)',
                ( name, email, contact_no, gender, dob, doj, salary, address, department, user_type))
            cursor.execute("commit")

            self.emp_id.set("Emp No")
            self.entry_name.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_contact_no.delete(0, 'end')
            self.cmb_gender.current(0)
            self.entry_dob.delete(0, 'end')
           # self.entry_dob.set_date('2-6-2022')
            self.entry_doj.delete(0, 'end')
            self.entry_salary.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.cmb_department.current(0)
            self.user_type_entry.delete(0, 'end')

            self.fetch()
            messagebox.showinfo("Insert Status", "Insert SucessFUlly")
            con.close()

    def update(self,event):
            x=0
            emp_id = self.entry_emp_id.get()
            name = self.entry_name.get()
            email = self.entry_email.get()
            contact_no = self.entry_contact_no.get()
            gender = self.cmb_gender.get()
            dob = self.entry_dob.get()
            doj = self.entry_doj.get()
            salary = self.entry_salary.get()
            address = self.entry_address.get()
            department = self.cmb_department.get()
            user_type = self.user_type_entry.get()
            if (
                    emp_id == "" or name == "" or email == "" or contact_no == "" or gender == "" or dob == "" or doj == "" or salary == "" or address == "" or department == "" or user_type == ""):
                messagebox.showerror("Update Status", "All Flieds Are Requried")
            elif len(contact_no) < 10:
                messagebox.showwarning("Alert", "Contact Number Should Be 10 Character")
            elif len(contact_no) > 10:
                messagebox.showwarning("Alert", "Contact Number Only 10 Character")
            elif self.email.get() != None:
                x = self.checkemail(self.email.get())
            if (x == True):
                con = mysql.connect(host="localhost", user="root", password="", database="ims")
                cursor = con.cursor()
                cursor.execute(
                    "update employee set name='" + name + "',email='" + email + "',contact_no='" + contact_no + "',gender='" + gender + "',dob='" + dob + "',doj='" + doj + "',salary='" + salary + "',address='" + address + "',department='" + department + "',user_type='" + user_type + "' where emp_id='" + emp_id + "'")
                cursor.execute("commit")

                self.emp_id.set("Emp No")
                self.entry_name.delete(0, 'end')
                self.entry_email.delete(0, 'end')
                self.entry_contact_no.delete(0, 'end')
                self.cmb_gender.current(0)
                self.entry_dob.delete(0, 'end')
                self.entry_doj.delete(0, 'end')
                self.entry_salary.delete(0, 'end')
                self.entry_address.delete(0, 'end')
                self.cmb_department.current(0)
                self.user_type_entry.delete(0, 'end')
                self.fetch()
                messagebox.showinfo("Update Status", "Updated SucessFully")
                con.close()

    def delete(self,event):
        if (self.entry_emp_id.get() == ""):
            messagebox.showerror("Delete", "Delete Requried")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute("delete from employee where emp_id='" + self.entry_emp_id.get() + "'")
            cursor.execute("commit")

            self.emp_id.set("Emp No")
            self.entry_name.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_contact_no.delete(0, 'end')
            self.cmb_gender.current(0)
            self.entry_dob.delete(0, 'end')
            self.entry_doj.delete(0, 'end')
            self.entry_salary.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.cmb_department.current(0)
            self.user_type_entry.delete(0, 'end')
            self.fetch()
            messagebox.showinfo("Delete Status", "Delete SucessFully")
            con.close()

    def clear_all(self,event):
        con = mysql.connect(host="localhost", user="root", password="", database="ims")
        cursor = con.cursor()
        cursor.execute("commit")
        emp_id = self.emp_id.set("Emp No")
        name =   self.entry_name.delete(0, 'end')
        email =   self.entry_email.delete(0, 'end')
        contact_no = self.entry_contact_no.delete(0, 'end')
        gender =  self.cmb_gender.current(0)
        dob = self.entry_dob.delete(0, 'end')
        doj = self.entry_doj.delete(0, 'end')
        salary = self.entry_salary.delete(0, 'end')
        address =  self.entry_address.delete(0, 'end')
        department = self.cmb_department.current(0)
        messagebox.showinfo("Inform", "Data will be clear")
        con.close()


    def search_data(self,event):
            con = mysql.connect(host="localhost", user="root", password="", database="ims")
            cursor = con.cursor()
            cursor.execute(
                "select *from employee where " + str(self.var_search_by.get()) + " LIKE '%" + str(
                    self.var_search_text.get()) + "%'")
            self.cmb_search.current(0)
            self.txt_search.delete(0, 'end')
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.tabel.delete(*self.tabel.get_children())
                for row in rows:
                    self.tabel.insert('', END, values=row)
                    con.commit()
                    messagebox.showinfo("info","data will be found")
                    con.close()
            else:
                messagebox.showerror("Error", "data will be not  found")





    def export_1(self,event):
        file = filedialog.asksaveasfilename()
        get = self.tabel.get_children()
        first, second, third, four, fifth, six, seven, eight, nine, ten, eleven = [], [], [], [], [], [], [], [], [], [], []
        dd = ['Emp No', 'Name', 'Email', 'Contact No', 'Gender', 'D.O.B', 'D.O.J', 'Salary', 'Address', 'Department',
              'User Type']
        for i in get:
            content = self.tabel.item(i)
            val = content['values']
            first.append(val[0]), second.append(val[1]), third.append(val[2]), four.append(val[3]), fifth.append(
                val[4]), six.append(val[5]),
            seven.append(val[6]), eight.append(val[7]), nine.append(val[8]), ten.append(val[9]), eleven.append(val[10])

        df = pandas.DataFrame(list(zip(first, second, third, four, fifth, six, seven, eight, nine, ten, eleven)),
                              columns=dd)
        paths = r'{}.csv'.format(file)
        df.to_csv(paths, index=False)
        messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

    def get_data(self, event):
        cur = self.tabel.focus()
        left = self.tabel.item(cur)
        row = left['values']

        self.emp_id.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.contact_no.set(row[3])
        self.gender.set(row[4])
        self.dob.set(row[5])
        self.doj.set(row[6])
        self.salary.set(row[7])
        self.address.set(row[8])
        self.department.set(row[9])
        self.user_type.set(row[10])

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

    def all_show(self,event):
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

            messagebox.showinfo("info", "All data in the display")




if __name__=="__main__":

    root=Tk()
    obj=employeeclass(root)
    root.mainloop()