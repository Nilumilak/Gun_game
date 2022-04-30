import tkinter as tk
from Character import Character
from Gun import Gun


def frame():

    ball.move()
    ball.jump()

    gun.move()
    gun.jump()
    gun.move_gun()

    top.after(50, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character(canvas)
ball.create()

gun = Gun(canvas)
gun.create()

frame()

top.mainloop()
