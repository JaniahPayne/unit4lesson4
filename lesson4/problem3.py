from turtle import *

pidge = Turtle()

pidge.color('blue')
pidge.pensize(6)
pidge.speed(8)
pidge.shape('turtle')

for x in range(6):
	pidge.forward(80)
	pidge.left(60)

mainloop()