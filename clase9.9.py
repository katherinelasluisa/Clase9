#ejercicio de imagen
from tkinter import *
tk= Tk()
canvas= Canvas(tk, width=400, height=400)
canvas.pack()

my_image= PhotoImage(file="ball.gif")
canvas.create_image(0,0, anchor=NW, image=my_image)
canvas.create_image(80,10, anchor=NW, image=my_image)
canvas.create_image(50,60, anchor=NW, image=my_image)
canvas.create_image(90,55, anchor=NW, image=my_image)
canvas.create_image(80,80, anchor=NW, image=my_image)
tk.mainloop()