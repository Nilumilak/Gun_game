import tkinter as tk
import Character
import Gun
import Bullet
import Targets


def frame():
    ball.move()
    ball.jump()

    gun.move()
    gun.jump()
    gun.move_gun()

    canvas.bind('<Button-1>', lambda trigger: Bullet.create_bullets(canvas, gun.gun_end_x_axis,  # creates bullets
                                                                    gun.gun_end_y_axis, gun.x_axis,
                                                                    gun.y_axis, trigger))
    [shell.bullet_fly() for shell in Bullet.bullets if Bullet.bullets]
    Bullet.delete_bullets(canvas)

    Targets.create_targets(canvas)
    [target.move() for target in Targets.targets if Targets.targets]
    Targets.delete_targets(canvas, Bullet.bullets)

    top.after(30, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character.Character(canvas)
ball.create()

gun = Gun.Gun(canvas)
gun.create()

frame()

top.mainloop()
