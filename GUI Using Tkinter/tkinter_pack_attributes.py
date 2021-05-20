from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

date = datetime.utcnow()

window_root = Tk()
window_root.geometry("1000x500")
window_root.minsize(900, 500)
window_root.title("tkinter pack attributes")

head_label = Label(text="Wel-come", bg="orange", font="Helvetica 16 bold")
head_label.pack(side=TOP, fill=X)

bottom_label = Label(text="Exit", bg="green", font="Helvetica 12 bold")
bottom_label.pack(side=BOTTOM, fill=X)

left_label = Label(text="Left Side", bg="white", fg="black",padx=30, font=("Helvetica", 12, "bold", "italic"))
left_label.pack(side=LEFT, fill=Y)

right_label = Label(text="Right Side", bg="white", fg="black",padx=30, font=("Helvetica", 12, "bold", "italic"))
right_label.pack(side=RIGHT, fill=Y)
img = Image.open("js-post.jpg")
photo = ImageTk.PhotoImage(img)
photo_label = Label(image=photo)
photo_label.pack(side=TOP,anchor=NE)
date_label = Label(text=date, font=("Helvetica", 10, "bold", "italic"), fg="Blue")
date_label.pack(side=BOTTOM, anchor=SE)




window_root.mainloop()
