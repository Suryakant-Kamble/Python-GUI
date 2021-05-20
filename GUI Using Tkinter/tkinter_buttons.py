from tkinter import *

root = Tk()

def hello():
   a= 1+2
   print(a,end=" ")


root.geometry("500x500")

f_frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f_frame.pack(side=LEFT, anchor=NE)

b1 = Button(f_frame, text="1", fg="black", command=hello)
b1.pack(side=LEFT,padx=2)

b2 = Button(f_frame, text="1", fg="black", command=hello)
b2.pack(side=LEFT,padx=2)

b3 = Button(f_frame, text="1", fg="black", command=hello)
b3.pack(side=LEFT,padx=2)

b4 = Button(f_frame, text="1", fg="black", command=hello)
b4.pack(side=LEFT,padx=2)


root.mainloop()