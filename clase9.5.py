#ejercicio de una estrella de N puntas

import turtle
#para borrar la pantall at.reset()
#t= turtle.Pen()
#for x in range (1,38):
#	t.forward(100)
#	t.left(175)
#turtle.getscreen()._root.mainloop()


#para borrar la pantall at.reset()
t= turtle.Pen()
n= int(input('ingrese un numero'))
for x in range (1,n+1):
	t.forward(100)
	#t.left(180-36)
	t.left(180-72)
turtle.getscreen()._root.mainloop()