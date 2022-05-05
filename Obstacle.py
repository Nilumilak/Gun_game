from random import randint


class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas

        self.x_axis = 800
        self.y_axis = 600
        self.height = 50
        self.width = 50

        self.speed = 5

        self.item_id = canvas.create_polygon(self.x_axis, self.y_axis,
                                             self.x_axis + self.width//2, self.y_axis - self.height,
                                             self.x_axis + self.width, self.y_axis)

    def move(self):
        self.x_axis -= self.speed
        self.canvas.move(self.item_id, -self.speed, 0)

    def delete_obstacle(self):
        self.canvas.delete(self.item_id)


def create_obstacles(canvas):
    global obstacles
    chance = randint(0, 150)
    if chance == 1:
        obstacles.append(Obstacle(canvas))


def delete_obstacles():
    for obstacle in obstacles:
        if obstacle.x_axis + obstacle.width < 0:
            obstacle.delete_obstacle()
            obstacles.remove(obstacle)


obstacles = []
