from tkinter import *

name_root = Tk()

name_root.minsize(800, 300)
name_root.maxsize(800, 300)
name_root.title("tkinter: Attributes of Label")

# Also you can use like: font="Helvetica 12 bold"
# relief means border styling i.e SUNKEN,RIDGE, RAISED,GROOVE
para_label = Label(text="Return system configuration information relevant to a named file."
                        "\nname specifies the configuration value to retrieve;"
                        "\nit may be a string which is the name of a defined system value; "
                        "\nthese names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others)."
                        "\nSome platforms define additional names as well."
                        "\nThe names known to the host operating system are given in the pathconf_names dictionary."
                        "\n For configuration variables not included in that mapping,"
                        "\npassing an integer for name is also accepted.",
                        bg="yellow", foreground="blue",
                        font=("Helvetica", "12", "bold"), padx=10, pady=60,
                        borderwidth=40, relief=SUNKEN
                   )



para_label.pack()








name_root.mainloop()