# import tkinter as tk
# root = tk.Tk()
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap',1,2,3]
#
# listb  = tk.Listbox(root)
# listb2 = tk.Listbox(root)
#
# for item in li:
#     listb.insert(0,item)
#
# for item in movie:
#     listb2.insert(0, item)
#
# listb.pack()
# listb2.pack()
# root.mainloop()

from tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()