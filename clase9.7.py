#poligono
import turtle
t= turtle.Pen()
angulo= int(input('ingrese el numero de lados'))
lados =int(input('ingrese el tamaño de lados'))
def mipoligono(numero,tamaño):
	for x in range (1,numero+1):
		t.forward(lado)
		t.left(360/numero)

mipoligono(angulo, lados)
turtle.getscreen()._root.mainloop()