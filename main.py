import tkinter as tk
from Character import Character
from Gun import Gun
from Bullet import Bullet


def create_bullets(event):
    global bullets
    if event:
        bullets.append(Bullet(canvas, gun.gun_end_x_axis, gun.gun_end_y_axis, gun.x, gun.y))
        bullets[-1].create()


def delete_objects():
    for shell in bullets:
        if shell.x > 900 or shell.x < -100 or shell.y > 700 or shell.y < -100:
            shell.delete_bullet()
            canvas.delete(shell)
            bullets.remove(shell)


def frame():
    ball.move()
    ball.jump()

    gun.move()
    gun.jump()
    gun.move_gun()

    canvas.bind('<Button-1>', create_bullets)               # creates bullets
    [shell.bullet_fly() for shell in bullets if bullets]

    delete_objects()

    top.after(30, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character(canvas)
ball.create()

gun = Gun(canvas)
gun.create()

bullets = []

frame()

top.mainloop()
