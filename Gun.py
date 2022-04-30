from Character import Character
import math


class Gun(Character):
    def __init__(self, canvas):
        Character.__init__(self, canvas)
        self.gun_end_x_axis = None
        self.gun_end_y_axis = None

    def create(self):
        self.item_id = self.canvas.create_line(self.x, self.y, self.x + (2 * self.R),
                                               self.y, fill='red', width=30)

    def move_gun(self):
        def motion(event):
            if event.x > self.x:
                angle = math.atan((event.y - self.y) / (event.x - self.x))
            elif event.x == self.x:
                angle = -math.pi / 2
            else:
                angle = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi
                
            self.gun_end_x_axis = self.x + self.R * 2 * math.cos(angle)
            self.gun_end_y_axis = self.y + self.R * 2 * math.sin(angle)

            self.canvas.coords(self.item_id, self.x, self.y,
                               self.gun_end_x_axis, self.gun_end_y_axis)

        self.canvas.bind('<Motion>', motion)

