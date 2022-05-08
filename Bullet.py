class Bullet:
    def __init__(self, canvas, gun_end_x_axis, gun_end_y_axis, gun_x, gun_y):
        self.canvas = canvas

        self.item_id = None

        self.bullet_speed_x_axis = (gun_end_x_axis - gun_x) // 5
        self.bullet_speed_y_axis = (gun_end_y_axis - gun_y) // 5

        self.x_axis = gun_end_x_axis
        self.y_axis = gun_end_y_axis
        self.R = 15

    def create(self):
        self.item_id = self.canvas.create_oval(self.x_axis - self.R,
                                               self.y_axis - self.R,
                                               self.x_axis + self.R,
                                               self.y_axis + self.R,
                                               fill='green')

    def bullet_fly(self):
        self.x_axis += self.bullet_speed_x_axis
        self.y_axis += self.bullet_speed_y_axis
        self.canvas.move(self.item_id, self.bullet_speed_x_axis, self.bullet_speed_y_axis)

    def delete_bullet(self):
        self.canvas.delete(self.item_id)


def create_bullets(canvas, gun_end_x_axis, gun_end_y_axis, x_axis, y_axis, event):
    global bullets
    if event:
        bullets.append(Bullet(canvas, gun_end_x_axis, gun_end_y_axis, x_axis, y_axis))
        bullets[-1].create()


def delete_bullets():
    for shell in bullets:
        if shell.x_axis > 900 or shell.x_axis < -100 or shell.y_axis > 700 or shell.y_axis < -100:
            shell.delete_bullet()
            bullets.remove(shell)


bullets = []
