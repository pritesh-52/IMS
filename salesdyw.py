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

class Salesdyw:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x600")
        self.root.config(bg="white")
        self.root.maxsize(700,600)


        lb=Label(root,text="Sales forecasting Yearly, Daywise, Weekly",font=('times new roman',18),fg="black",bg="white")
        lb.place(x=90)
        self.image3 = Image.open('images/SALES_PREDITION_2.png')
        self.image3 = self.image3.resize((620, 500), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.new3 = Label(root, image=self.photo3)
        self.new3.place(x=30, y=30)




if __name__ == '__main__':
    root=Tk()
    obj=Salesdyw(root)
    root.mainloop()
