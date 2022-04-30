from Gun import Gun


class Bullet(Gun):
    def __init__(self, canvas, gun_end_x_axis, gun_end_y_axis, gun_x, gun_y):
        Gun.__init__(self, canvas)
        self.bullets = []
        self.bullet_start_position_x_axis = gun_end_x_axis
        self.bullet_start_position_y_axis = gun_end_y_axis
        self.gun_position_x_axis = gun_x
        self.gun_position_y_axis = gun_y
        self.R = 15

    def create(self):
        self.item_id = self.canvas.create_oval(self.bullet_start_position_x_axis - self.R,
                                               self.bullet_start_position_y_axis - self.R,
                                               self.bullet_start_position_x_axis + self.R,
                                               self.bullet_start_position_y_axis + self.R,
                                               fill='green')

    def bullet_fly(self):
        bullet_speed_x_axis = (self.bullet_start_position_x_axis - self.gun_position_x_axis) // 5
        bullet_speed_y_axis = (self.bullet_start_position_y_axis - self.gun_position_y_axis) // 5
        self.x += bullet_speed_x_axis
        self.y += bullet_speed_y_axis
        self.canvas.move(self.item_id, bullet_speed_x_axis, bullet_speed_y_axis)

    def delete_bullet(self):
        self.canvas.delete(self.item_id)

