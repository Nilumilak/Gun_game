import keyboard


class Character:
    def __init__(self, canvas):
        self.canvas = canvas

        self.item_id = None

        self.x_axis = 300
        self.y_axis = 550
        self.R = 50
        self.speed = 5

        self.jump_speed = 3
        self.max_jump_height = 10
        self.ground_position = self.max_jump_height * self.jump_speed
        self.jump_position = self.max_jump_height * self.jump_speed

    def create(self):
        self.item_id = self.canvas.create_oval(self.x_axis - self.R, self.y_axis - self.R,
                                               self.x_axis + self.R, self.y_axis + self.R,
                                               fill='black')

    def move(self):
        if keyboard.is_pressed('a'):
            if self.x_axis > 2 + self.R:
                speed_back = -self.speed
                self.x_axis += speed_back
                self.canvas.move(self.item_id, speed_back, 0)
        if keyboard.is_pressed('d'):
            if self.x_axis < 800 - self.R:
                self.x_axis += self.speed
                self.canvas.move(self.item_id, self.speed, 0)

    def jump(self):
        if keyboard.is_pressed('w'):
            self.jump_position -= self.jump_speed
            self.y_axis -= self.jump_position
            self.canvas.move(self.item_id, 0, -self.jump_position)
            if self.jump_position <= -(self.ground_position - self.jump_speed):
                self.jump_position = self.ground_position
                self.y_axis = 550
        else:
            if (self.jump_position >= -(self.ground_position - self.jump_speed * 2)
                    and self.jump_position != self.ground_position):
                self.jump_position -= self.jump_speed
                self.y_axis -= self.jump_position
                self.canvas.move(self.item_id, 0, -self.jump_position)
            else:
                self.jump_position = self.ground_position
                self.y_axis = 550
                self.canvas.coords(self.item_id, self.x_axis - self.R, self.y_axis - self.R,
                                   self.x_axis + self.R, self.y_axis + self.R)
