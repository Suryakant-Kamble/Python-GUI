from tkinter import *

root = Tk()

users = "suryakant"
passwords = "123456"


def login():
    entry_user_id = user_value.get()
    entry_password = password_value.get()
    # entry_mark = remember_value.get()
    if users == entry_user_id and passwords == entry_password:
        print("Successfully login")


root.minsize(375, 285)
root.maxsize(375, 285)
root.iconbitmap("ad_icon.ico")
root.title("Admin Login Panel")

f_frame = Frame(root, bg="pink", relief=SUNKEN, bd=4, )
f_frame.pack()
f_label = Label(f_frame, text="Admin Login Panel", font="helvetica 18 bold", bg="pink")
f_label.pack(pady=20)

_frame = Frame(f_frame, bg="yellow", relief=SUNKEN, borderwidth=4)
_frame.pack(pady=20, padx=20)

txt_label = Label(_frame, text="Please Enter your login Details", font="helvetica 16 bold", bg="yellow")
txt_label.grid(row=0, columnspan=8, pady=8)

user = Label(_frame, text="User Name", bg="yellow", font="Helvetica 12 bold")
password = Label(_frame, text="Password", bg="yellow", font="Helvetica 12 bold")
user.grid(row=1, pady=4)
password.grid(row=2, pady=4)

user_value = StringVar()
password_value = StringVar()
remember_value = IntVar()

user_entry = Entry(_frame, textvariable=user_value, font="Helvetica 12 bold")
password_entry = Entry(_frame, textvariable=password_value, font="Helvetica 12 bold")
user_entry.grid(row=1, column=1, pady=4)
password_entry.grid(row=2, column=1, pady=4)

chk_button = Checkbutton(_frame, text="Remember", variable=remember_value, bg="yellow", font="Helvetica 10 bold")
chk_button.grid(row=3, column=0, pady=4)
login_button = Button(_frame, text="Log In", font="Helvetica 12 bold", command=login)
login_button.grid(row=3, column=1, pady=4)

root.mainloop()
