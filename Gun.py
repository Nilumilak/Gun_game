from Character import Character
import math


class Gun(Character):
    def create(self):
        self.item_id = self.canvas.create_line(self.x, self.y, self.x + (2 * self.R),
                                               self.y, fill='red', width=30)

    def move_gun(self):
        x = self.x
        y = self.y

        def motion(event):
            if event.x > self.x:
                angle = math.atan((event.y - self.y) / (event.x - self.x))
            elif event.x == self.x:
                angle = -math.pi / 2
            else:
                angle = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi
            print(angle)
            self.canvas.coords(self.item_id, x, y,
                               x + self.R * 2 * math.cos(angle), y + self.R * 2 * math.sin(angle))

        self.canvas.bind('<Motion>', motion)
