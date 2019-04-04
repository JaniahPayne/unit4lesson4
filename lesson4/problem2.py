from turtle import *

pidge = Turtle()

pidge.color('orange')
pidge.pensize(5)
pidge.speed(5)
pidge.shape('turtle')
pidge.turtlesize(5,5,5)

for x in range(4):
	pidge.forward(100)
	pidge.left(90)
	
	

mainloop()
