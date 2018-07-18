import turtle
wn = turtle.Screen() # Creates a playground for turtles
haigui = turtle.Turtle() # Create a turtle, assign to alex
haigui.speed(0)
def drawOutline():
    haigui.penup()
    haigui.goto(0,200)
    haigui.pendown()
    haigui.goto(-200, 0)
    haigui.penup()
    haigui.goto(0, 200)
    haigui.pendown()
    haigui.goto(200, 0)
    haigui.penup()
    haigui.goto(-160, 40)
    haigui.pendown()
    haigui.right(90)
    haigui.forward(240)
    haigui.left(90)
    haigui.forward(320)
    haigui.left(90)
    haigui.forward(240)

def drawDoor():
    drawSquareFrame(-50,-200,'green',100)
    drawKnot(30, -160, 10)

def drawChimney():
    haigui.penup()
    haigui.goto(100,150)
    haigui.pendown()
    haigui.goto(150,150)
    haigui.goto(150,50)
    haigui.goto(100,100)
    haigui.goto(100,150)

def drawSquareFrame(x,y,color='blue',size=30):
    haigui.fillcolor(color)
    haigui.penup()
    haigui.begin_fill()
    haigui.goto(x,y)
    haigui.pendown()
    for i in range(4):
        haigui.forward(size)
        haigui.right(90)
    haigui.end_fill()

def drawWindow(x,y,color='blue',size=30):
    drawSquareFrame(x,y,color,size)
    drawSquareFrame(x + size, y,color, size)
    drawSquareFrame(x + size, y+size, color, size)
    drawSquareFrame(x , y + size, color, size)

def drawWindows():
    drawWindow(-30, 60,'blue')
    drawWindow(-130, -60, 'orange')
    drawWindow(70, -60, 'yellow')

def drawKnot(x,y,knotSize = 10):
    haigui.fillcolor('red')
    haigui.penup()
    haigui.begin_fill()
    haigui.goto(x,y)
    haigui.pendown()
    haigui.circle(knotSize)
    haigui.end_fill()

def drawHouse():
    drawOutline()
    drawDoor()
    drawChimney()
    drawWindows()

drawHouse()
wn.mainloop()