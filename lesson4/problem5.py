from turtle import *

pidge = Turtle()

pidge.color('orange')
pidge.pensize()
pidge.speed(3)
pidge.shape('turtle')

def drawHexagon():
	for x in range(6):
		pidge.forward(30)
		pidge.left(60)

for x in range(12):
	drawHexagon()
	pidge.left(30)

	

mainloop()