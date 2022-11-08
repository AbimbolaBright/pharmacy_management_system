from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os
# import tititi as TT
import mysql.connector as mysql
from mysql.connector.errors import Error

root = Tk()
root.title("Pharmacy Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



Top = Frame(root, width=900, height=50 ,bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8, relief="raise")

Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=250, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)


txt_title = Label(Top, width=900, font=('arial', 24),fg='red',text = "Pharmacy Management System")
txt_title.pack()
label0 = Label(Forms, text="Medicine Name:", fg='red',font=('arial', 16), bd=15)
label0.grid(row=0, stick="e")
label1 = Label(Forms, text="Medicine Price:",fg='red', font=('arial', 16), bd=15)
label1.grid(row=1, stick="e")
label2 = Label(Forms, text="Quantity:",fg='red', font=('arial', 16), bd=15)
label2.grid(row=2, stick="e")
label3 = Label(Forms, text="Category:",fg='red', font=('arial', 16), bd=15)
label3.grid(row=3, stick="e")
label4 = Label(Forms, text="Description:",fg='red', font=('arial', 16), bd=15)
label4.grid(row=4, stick="e")
label5 = Label(Forms, text="Discount:",fg='red', font=('arial', 16), bd=15)
label5.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)


entry1 = Entry(Forms, width=30)
entry1.grid(row=0, column=1) 
entry2 = Entry(Forms, width=30)
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, width=30)
entry3.grid(row=2, column=1)
entry4 = Entry(Forms,width=30)
entry4.grid(row=3, column=1)
entry5 = Entry(Forms, width=30)
entry5.grid(row=4, column=1)
entry6 = Entry(Forms, width=30)
entry6.grid(row=5, column=1)


root.mainloop()