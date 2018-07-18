from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
import numpy as np
from PIL import ImageColor


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="Welcome To the main Control: There will be three pages in total， \n each pages has its unique functionality just wait for you to explore \n now start choosing the picture you want to edit by clicking the button above", fg = "blue")
       label.pack(side="top", fill="both", expand=True)
       
       
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This page will tell you how to manipulate image : use the filter button below\n and apply different filter on to the displayed image then click on \nthe canvas to display the image onto the board",fg = "blue")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="If you want to save your masterpiece click save image\n then you can find the image in your finder",fg = "blue")
       label.pack(side="top", fill="both", expand=True)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        frame = Frame(root, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=E+W)
        yscroll = Scrollbar(frame)
        yscroll.grid(row=0, column=1, sticky=N+S)
        canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)
        xscroll.config(command=canvas.xview)
        yscroll.config(command=canvas.yview)
        frame.pack(fill=BOTH,expand=1)

        def image_entry1():
           global File
           File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
           global img
           img = ImageTk.PhotoImage(Image.open(File))
 #         canvas.create_image(0,0,image=img,anchor="nw")
           while 1: canvas.update()
           return img,File

        def image_entry2():
           File2 = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
           img2 = ImageTk.PhotoImage(Image.open(File2))
           canvas.create_image(540,100,image=img2,anchor="nw")
           while 1: canvas.update()                
        
        def printcoords(event):
            canvas.create_image(event.x,event.y,image=img,anchor="nw")
            
        canvas.bind("<Button 1>",printcoords)



        def clear():
            canvas.delete("all")
        



        def pencil(img, threshold):
            '''
            铅笔画
            param img: instance of Image
            param threshold
            '''
            if threshold < 0: threshold = 0
            if threshold > 100: threshold = 100
         
            width, height = img.size
            dst_img = Image.new("RGBA", (width, height))
         
            if img.mode != "RGBA":
                img = img.convert("RGBA")
         
            pix = img.load()
            dst_pix = dst_img.load()
         
            for w in xrange(width):
                for h in xrange(height):
                    if w == 0 or w == width - 1 \
                       or h == 0 or h == height - 1:
                        continue
         
                    # 包括当前像素周围共9个像素点
                    around_wh_pixels = [pix[i, j][:3] for j in xrange(h-1, h+2) for i in xrange(w-1, w+2)]
                    # 排除当前像素点
                    exclude_wh_pixels = tuple(around_wh_pixels[:4] + around_wh_pixels[5:])
                    # 把各个像素点的各个分量求平均值          
                    RGB = map(lambda l: int(sum(l) / len(l)), zip(*exclude_wh_pixels))
                     
                    cr_p = pix[i, j] # 当前像素点
         
                    cr_draw = all([abs(cr_p[i] - RGB[i]) >= threshold for i in range(3)])
                    
                    if cr_draw:
                        dst_pix[w, h] = 0, 0, 0, cr_p[3]
                    else:
                        dst_pix[w, h] = 255, 255, 255, cr_p[3]
         
            return dst_img
        

        def filter1():
            global img
            global File
            img_temp = Image.open(File)
            img_temp = pencil(img_temp,10)
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")
        

        def sketch(img, threshold):
            if threshold < 0: threshold = 0
            if threshold > 100: threshold = 100
             
            width, height = img.size
            img = img.convert('L') # convert to grayscale mode
            pix = img.load() # get pixel matrix
         
            for w in xrange(width):
                for h in xrange(height):
                    if w == width-1 or h == height-1:
                        continue
                     
                    src = pix[w, h]
                    dst = pix[w+1, h+1]
         
                    diff = abs(src - dst)
         
                    if diff >= threshold:
                        pix[w, h] = 0
                    else:
                        pix[w, h] = 255
         
            return img

        def filter2():
            global img
            global File
            img_temp = Image.open(File)
            img_temp = sketch(img_temp,10)
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")

        def filter3():
            global File
            global img
            img_temp = Image.open(File)
            img_temp = img_temp.convert("L")
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")

        def filter4():
            global File
            global img
            img_temp = Image.open(File)
            img_temp = img_temp.convert("1")
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")
        
        def chooseimage2():
            global img
            global File

 #       Button(root, text )

        def save():           
            canvas.postscript(file="my_drawing.ps", colormode='color')
 
        def twi():
            global File
            global img
            img_temp = Image.open(File)
            (X, Y) = img_temp.size

            for x in range(X):
                for y in range(Y):
                    (r, g, b) = img_temp.getpixel((x, y))
                    img_temp.putpixel((x, y), (int(r * 0.3), int(g * 0.4), int(b * 0.5)))
                    
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")

        def pink():
            global File
            global img
            img_temp = Image.open(File)
            (X, Y) = img_temp.size

            for x in range(X):
                for y in range(Y):
                    (r, g, b) = img_temp.getpixel((x, y))
                    img_temp.putpixel((x, y), (int(b), int(r), int(g)))
                    
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")

        def vigour():
            global File
            global img
            img_temp = Image.open(File)
            (X, Y) = img_temp.size

            for x in range(X):
                for y in range(Y):
                    (r, g, b) = img_temp.getpixel((x, y))
                    img_temp.putpixel((x, y), (int(g), int(b), int(r)))
                    
            img = ImageTk.PhotoImage(img_temp)
            canvas.create_image(0,0,image=img,anchor="nw")

########################################################     BUTTONS   ##########################################


        buttonframe2 = Frame(root)
        buttonframe2.pack(side="bottom", fill="x", expand=False)
        Button(buttonframe2, text="choose the board image", command = image_entry2).pack()
        Button(buttonframe2, text="choose the display image", command = image_entry1).pack()
        Button(buttonframe2, text="clear board", command = clear).pack()
        Button(buttonframe2, text="Filter:pencil", command = filter1).pack()
        Button(buttonframe2, text="Filter:pink", command = pink).pack()
        Button(buttonframe2, text="Filter:vigour", command = vigour).pack()
        Button(buttonframe2, text="Filter:gray", command = filter3).pack()
        Button(buttonframe2, text="Filter:Twilight", command = twi).pack()
        Button(buttonframe2, text="saveimg", command = save).pack()

########################################################     framecontrol   ##########################################


        
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()
        
if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()













