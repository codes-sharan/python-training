# GUI in Python 

import tkinter as tk

root = tk.Tk()

root.title("My First App")

root.geometry("400x300")

label = tk.Label(root, text="Hello Nepal")

label.pack()

root.mainloop()