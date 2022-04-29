import tkinter as tk
from Character import Character


def frame():
    ball.jump()
    ball.move()
    top.after(50, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character(canvas)
frame()

top.mainloop()
