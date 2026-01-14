import turtle

turtle.Screen().bgcolor('oldlace')

w=turtle.Screen()
w.setup(400,300)

turtle.title('First turtle program')

w=turtle.Turtle()
w.speed(3)
w.pensize(2)
w.pencolor('black')
w.fillcolor('red')
w.begin_fill()
w.forward(100)
w.left(90)
w.forward(100)
w.left(90)
w.forward(100)
w.left(90)
w.forward(100)
w.left(90)
w.end_fill()
w.penup()
w.goto(-80,-90)
w.pendown()

w.fillcolor('pink')
w.begin_fill()
w.forward(80)
w.right(120)
w.forward(80)
w.right(120)
w.forward(80)
w.right(120)
w.end_fill()





turtle.done()