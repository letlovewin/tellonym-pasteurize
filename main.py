import tkinter as tk

#from tkinter import ttk
from spammer import spam

window = tk.Tk()
window.iconphoto(False,tk.PhotoImage(file="favicon.png"))
window.title("PASTEURIZE")
window.minsize(300,150)
window.resizable(False,False)

info = tk.Label(text="Buries search results related to your name.")
firstname_label = tk.Label(text="First Name")
lastname_label = tk.Label(text="Last Name")
firstname_entry = tk.Entry()
lastname_entry = tk.Entry()
begin_button = tk.Button(text="Start burying",command=spam)

info.pack()
firstname_label.pack()
firstname_entry.pack()
lastname_label.pack()
lastname_entry.pack()
begin_button.pack()

window.mainloop()