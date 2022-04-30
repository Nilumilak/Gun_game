import tkinter as tk
from Character import Character
from Gun import Gun
from Bullet import Bullet


def frame():
    ball.move()
    ball.jump()

    gun.move()
    gun.jump()
    gun.move_gun()

    # bullet.create()
    canvas.bind('<Button-1>', bullet.create)
    bullet.gun_end_coordinates(gun.gun_end_x_axis, gun.gun_end_y_axis)
    if bullet.item_id:
        bullet.bullet_fly()

    top.after(30, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character(canvas)
ball.create()

gun = Gun(canvas)
gun.create()

bullet = Bullet(canvas)

frame()

top.mainloop()
