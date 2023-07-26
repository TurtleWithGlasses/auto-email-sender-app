from tkinter import *
import smtplib
import re


root = Tk()
root.title("Email Application")

f1 = Frame(root, width=1000, height=800)
f1.pack(side=TOP)

label1 = Label(f1, width=25, text="Enter your credentials", font=("Arial 18 bold"))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, width=25, text="Email")
label2.grid(row=1, sticky=E, pady=5, padx=10)

label3 = Label(f1, width=25, text="Password")
label3.grid(row=2, sticky=E, pady=5, padx=10)

email_entry = Entry(f1)
password_entry = Entry(f1, show="*")

email_entry.grid(row=1, column=1, pady=5)
password_entry.grid(row=2, column=1)

button1 = Button(f1, text="Login", width=10, bg="black", fg="white", command= lambda : login())
button1.grid(row=3, columnspan=3, pady=10)