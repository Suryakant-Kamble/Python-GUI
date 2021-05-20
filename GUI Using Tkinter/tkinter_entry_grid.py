from tkinter import *

root = Tk()


def getvalue():
    username = uservalue.get()
    upassword = passvalue.get()
    print(username, upassword)



root.geometry("600x500")
user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()


userentry= Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

b1 = Button(root, text="Submit", command=getvalue)
b1.grid()

root.mainloop()
