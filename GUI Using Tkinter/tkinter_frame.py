from tkinter import *

root = Tk()

root.geometry("500x500")

f1_frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f1_frame.pack(side=LEFT, fill=Y)
f2_frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f2_frame.pack(fill=X)

f1_label=Label(f1_frame, text="TKinter Pycharm" )
f1_label.pack(pady=150)
f2_label=Label(f2_frame, text="NOTEPADE++")
f2_label.pack()




root.mainloop()