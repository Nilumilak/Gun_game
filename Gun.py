from Character import Character
import math
import keyboard


class Gun(Character):
    def __init__(self, canvas):
        Character.__init__(self, canvas)
        self.gun_end_x_axis = self.x_axis + (2 * self.R)
        self.gun_end_y_axis = self.y_axis

    def create(self):
        self.item_id = self.canvas.create_line(self.x_axis, self.y_axis, self.x_axis + (2 * self.R),
                                               self.y_axis, fill='red', width=30)

    def move(self):
        if keyboard.is_pressed('a'):
            if self.x_axis > 2 + self.R:
                speed_back = -self.speed
                self.x_axis += speed_back
                self.gun_end_x_axis += speed_back
                self.canvas.move(self.item_id, speed_back, 0)
        if keyboard.is_pressed('d'):
            if self.x_axis < 800 - self.R:
                self.x_axis += self.speed
                self.gun_end_x_axis += self.speed
                self.canvas.move(self.item_id, self.speed, 0)

    def jump(self):
        if keyboard.is_pressed('w'):
            self.jump_position -= self.jump_speed
            self.y_axis -= self.jump_position
            self.gun_end_y_axis -= self.jump_position
            self.canvas.move(self.item_id, 0, -self.jump_position)
            if self.jump_position <= -(self.ground_position - self.jump_speed):
                self.jump_position = self.ground_position
                self.y_axis = 550
        else:
            if (self.jump_position >= -(self.ground_position - self.jump_speed * 2)
                    and self.jump_position != self.ground_position):
                self.jump_position -= self.jump_speed
                self.y_axis -= self.jump_position
                self.gun_end_y_axis -= self.jump_position
                self.canvas.move(self.item_id, 0, -self.jump_position)
            else:
                self.jump_position = self.ground_position
                self.y_axis = 550
                self.canvas.coords(self.item_id, self.x_axis, self.y_axis,
                                   self.gun_end_x_axis, self.gun_end_y_axis)

    def move_gun(self):
        def motion(event):
            if event.x > self.x_axis:
                angle = math.atan((event.y - self.y_axis) / (event.x - self.x_axis))
            elif event.x == self.x_axis:
                angle = -math.pi / 2
            else:
                angle = math.atan((event.y - self.y_axis) / (event.x - self.x_axis)) + math.pi
                
            self.gun_end_x_axis = self.x_axis + self.R * 2 * math.cos(angle)
            self.gun_end_y_axis = self.y_axis + self.R * 2 * math.sin(angle)

            self.canvas.coords(self.item_id, self.x_axis, self.y_axis,
                               self.gun_end_x_axis, self.gun_end_y_axis)

        self.canvas.bind('<Motion>', motion)

