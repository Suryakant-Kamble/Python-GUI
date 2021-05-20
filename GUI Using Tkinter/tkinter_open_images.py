from tkinter import *
from PIL import Image, ImageTk

# Tkinter supports PNG images only, that why we use PIL
s_root = Tk()
s_root.geometry("700x700")            # Geometry: set your window screen, width x height
s_root.minsize(600, 600)             # minsize: set minimum size screen width=300, height  ( s_root.maxsize(600, 600))
s_root.title("Tkinter_Open_images")            # title: window name(title)

# Use Tkinter ,  For PNG format

png_photo = PhotoImage(file="html-post.png")
png_label = Label(image=png_photo)
png_label.pack()

# Use PIL, For jpg format and also supports png images
img = Image.open("js-post.jpg")
photo = ImageTk.PhotoImage(img)
i_label=Label(image=photo)
i_label.pack()



s_root.mainloop()
