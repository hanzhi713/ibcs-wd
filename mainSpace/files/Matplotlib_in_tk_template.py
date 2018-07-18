import matplotlib
matplotlib.use('TkAgg')
import cv2
import matplotlib.pyplot as plt
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.geometry("800x1000")
root.wm_title("Embedding in TK")

global mousePos, clickPoints, pixelValue
mousePos = []
clickPoints = []
pixelValue = []
im = cv2.imread("testimg.jpg")
b,g,r = cv2.split(im)
im2 = cv2.merge([r,g,b])
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
a.imshow(im2)

imgsize = im2.shape

def format_coord(x, y):
    col = int(x+0.5)
    row = int(y+0.5)
    if col>=0 and col<imgsize[1] and row>=0 and row<imgsize[0]:
        z = im2[row,col]
        mousePos.append((col,row))
        pixelValue.append(z)
        return 'x={}, y={}, z={}'.format(round(x), round(y), z)

    else:
        return 'x=%1.4f, y=%1.4f'%(x, y)

a.format_coord = format_coord

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

def onclick(event):
    print('clicked!')
    value = mousePos.pop()
    pValue = pixelValue.pop()
    clickPoints.append(value)
    mousePos.clear()
    pixelValue.clear()
    print( value,':', pValue)
    listb.insert(0, ('pixel Pos:', value,'is: ', pValue))

canvas.mpl_connect('key_press_event', on_key_event)
canvas.mpl_connect('button_press_event', onclick)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)
listb  = Tk.Listbox(root)

listb.bind('<ButtonRelease-1>', onclick)
listb.pack(side=Tk.BOTTOM)
Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
