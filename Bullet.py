from Gun import Gun
import keyboard


class Bullet(Gun):
    def __init__(self, canvas):
        Gun.__init__(self, canvas)
        self.bullets = []

    def create(self, event):
        if event:
            bullet_R = self.R // 3
            # self.bullets.append(self.canvas.create_oval(self.gun_end_x_axis - bullet_R, self.gun_end_y_axis - bullet_R,
            #                                             self.gun_end_x_axis + bullet_R, self.gun_end_y_axis + bullet_R,
            #                                             fill='green'))

            self.item_id = self.canvas.create_oval(self.gun_end_x_axis - bullet_R, self.gun_end_y_axis - bullet_R,
                                                   self.gun_end_x_axis + bullet_R, self.gun_end_y_axis + bullet_R,
                                                   fill='green')
            print(self.item_id)

        # if len(self.bullets) > 5:
        #     self.canvas.delete(self.bullets[0])
        #     self.bullets.pop(0)

    def move(self):
        pass

    def jump(self):
        pass

    def gun_end_coordinates(self, gun_end_x_axis, gun_end_y_axis):
        self.gun_end_x_axis = gun_end_x_axis
        self.gun_end_y_axis = gun_end_y_axis

    def bullet_fly(self):
        bullet_fly_x_axis = (self.gun_end_x_axis - self.x) // 5
        bullet_fly_y_axis = (self.gun_end_y_axis - self.y) // 5
        self.canvas.move(self.item_id, bullet_fly_x_axis, bullet_fly_y_axis)
