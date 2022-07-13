import tkinter as tk
import Character
import Gun
import Bullet
import Targets
import Battlefield
import Obstacle


def frame():
    ball.move()
    ball.jump()

    gun.move()
    gun.jump()
    gun.move_gun()

    canvas.bind('<Button-1>', lambda trigger: Bullet.create_bullets(canvas, gun.gun_end_x_axis,  # creates bullets
                                                                    gun.gun_end_y_axis, gun.x_axis,
                                                                    gun.y_axis, battlefield_events, trigger))
    [shell.bullet_fly() for shell in Bullet.bullets if Bullet.bullets]
    Bullet.delete_bullets()
    if battlefield_events.life_numbers == 0:
        top.quit()

    Targets.create_targets(canvas)
    [target.move() for target in Targets.targets if Targets.targets]
    Targets.delete_targets(Bullet.bullets, battlefield_events)

    Obstacle.create_obstacles(canvas)
    [obstacle.move() for obstacle in Obstacle.obstacles if Obstacle.obstacles]
    Obstacle.delete_obstacles(ball, battlefield_events)

    top.after(30, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

battlefield_events = Battlefield.Battlefield(canvas)

ball = Character.Character(canvas)
ball.create()

gun = Gun.Gun(canvas)
gun.create()

frame()

top.mainloop()
