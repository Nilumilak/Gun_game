from random import randint
import math


class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas

        self.x_axis = 800
        self.y_axis = 600
        self.height = 50
        self.width = 50

        self.speed = 7

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
    chance = randint(0, 100)
    if chance == 1:
        if obstacles and obstacles[-1].x_axis < 600:
            obstacles.append(Obstacle(canvas))
        elif not obstacles:
            obstacles.append(Obstacle(canvas))


def delete_obstacles(character_position, battlefield_events):
    for obstacle in obstacles:
        if obstacle.x_axis + obstacle.width < 0:
            obstacle.delete_obstacle()
            obstacles.remove(obstacle)
        for obstacle in obstacles:
            distance = math.sqrt((character_position.x_axis - (obstacle.x_axis + obstacle.width//2)) ** 2
                                 + (character_position.y_axis - (obstacle.y_axis - obstacle.height)) ** 2)
            if distance < character_position.R:
                obstacle.delete_obstacle()
                obstacles.remove(obstacle)
                battlefield_events.life_counting()


obstacles = []
