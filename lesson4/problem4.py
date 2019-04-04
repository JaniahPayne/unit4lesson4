from turtle import *

Pidge = Turtle()

Pidge.color('orange')
Pidge.pensize(4)
Pidge.speed(4)
Pidge.shape('turtle')

Izzie = Turtle()

Izzie.color('red')
Izzie.pensize(4)
Izzie.speed(4)
Izzie.shape('turtle')

for x in range(3):
	Pidge.forward(60)
	Pidge.left(120)

Izzie.circle(100)


mainloop()
