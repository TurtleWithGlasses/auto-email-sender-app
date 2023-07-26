from tkinter import *
import smtplib
import re


def login():
    if validate_login():
        global username
        global password
        username = str(email_entry.get())
        password = str(password_entry.get())
        global server
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(username, password)
        login_page.pack()
        button2.grid()
        label4["text"] = "Logged in!"
        root.after(10, root.grid)
        main_page.pack_forget()
        root.after(10, root.grid)
        compose_page.pack()
        label9.grid_remove()
        root.after(10, root.grid)


def hide_login_label():
    login_page.pack_forget()
    compose_page.pack_forget()
    root.after(10, root.grid)


def send_mail():
    if validate_message():
        label9.grid_remove()
        root.after(10, root.grid)
        receiver = str(entry3.get())
        subject = str(entry4.get())
        msg_body = str(entry5.get())
        msg = f"From {username}\n{receiver}\n{subject}\n{msg_body}"

        try:
            server.sendmail(username, receiver, msg)
            label9.grid()
            label9["text"] = "Mail sent successfully"
            root.after(10, label9.grid)
        except Exception as e:
            label9.grid()
            label9["text"] = "Error in sending you email"
            root.after(10, label9.grid)


def logout():
    try:
        server.quit()
        compose_page.pack_forget()
        login_page.pack()
        label4.grid()
        label4["text"] = "Logged out successfully"
        button2.grid_remove()
        main_page.pack()
        password_entry.delete(0, END)
        root.after(10, root.grid)
    except Exception as e:
        label4["text"] = "Error in logout"


def validate_login():
    email_text = str(email_entry.get())
    pass_text = str(password_entry.get())

    if (email_text == "") or (pass_text == ""):
        login_page.pack()
        label4.grid()
        label4["text"] = "Fill all the empty fields"
        button2.grid_remove()
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            login_page.pack()
            label4.grid()
            label4["text"] = "Enter a valid email address"
            return False
        else:
            return True


def validate_message():
    email_text = str(entry3.get())
    sub_text = str(entry4.get())
    msg_text = str(entry5.get())

    if email_text == "" or sub_text == "" or msg_text == "":
        label9.grid()
        label9["text"] = "Fill in all the places"
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            label9.grid()
            label9["text"] = "Enter a valid email address"
            root.after(10, root.grid)
            return False
        elif (len(sub_text) < 3) or (len(msg_text) < 3):
            label9.grid()
            label9["text"] = "Enter at least 3 characters"
            root.after(10, root.grid)
            return False
        else:
            return True


root = Tk()
root.title("Email Application")

main_page = Frame(root, width=1000, height=800)
main_page.pack(side=TOP)

label1 = Label(main_page, width=25, text="Enter your credentials", font=("Arial 18 bold"))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(main_page, width=25, text="Email")
label2.grid(row=1, sticky=E, pady=5, padx=10)

label3 = Label(main_page, width=25, text="Password")
label3.grid(row=2, sticky=E, pady=5, padx=10)

email_entry = Entry(main_page)
password_entry = Entry(main_page, show="*")

email_entry.grid(row=1, column=1, pady=5)
password_entry.grid(row=2, column=1)

button1 = Button(main_page, text="Login", width=10, bg="black", fg="white", command=lambda: login())
button1.grid(row=3, columnspan=3, pady=10)


login_page = Frame(root)
login_page.pack(side=TOP, expand=NO, fill=NONE)

label4 = Label(login_page, width=20, bg="gray", fg="red", text="Login success", font="Arial 12 bold")
label4.grid(row=0, column=0, columnspan=2, pady=5)

button2 = Button(login_page, text="Logout", bg="black", fg="white", command=lambda: logout())
button2.grid(row=0, column=4, sticky=E, pady=10, padx=(5,0))

compose_page = Frame(master=root)
compose_page.pack(side=TOP, expand=NO, fill=NONE)

label5 = Label(compose_page, width=20, text="Compose Email", font=("Calibri 18 bold"))
label5.grid(row=0, columnspan=3, pady=10)

label6 = Label(compose_page, text="To").grid(row=1, sticky=E, pady=5)
label7 = Label(compose_page, text="Subject").grid(row=2, sticky=E, pady=5)
label8 = Label(compose_page, text="Message").grid(row=3, sticky=E)

entry3 = Entry(compose_page)
entry4 = Entry(compose_page)
entry5 = Entry(compose_page)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

send_button = Button(compose_page, text="Send Mail", width=10, bg="black", fg="white", command=lambda:send_mail())
send_button.grid(row=6, columnspan=3, pady=10)

label9 = Label(compose_page, width=20, fg="white", bg="black", font=("Calibri 18 bold"))
label9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()