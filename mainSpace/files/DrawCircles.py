import turtle
NumCircles = 10
CircleInterval = 20
turtle.home()
for i in range(1,1+NumCircles):
    turtle.pendown()
    turtle.circle(CircleInterval*i)
    turtle.penup()
    turtle.goto(0,-1*CircleInterval*i)
turtle.mainloop()