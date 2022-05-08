from random import randint, choice
import math


class Target:
    def __init__(self, canvas):
        self.canvas = canvas

        self.x_axis = randint(0, 800)
        self.y_axis = -50
        self.R = randint(10, 50)

        self.speed = randint(1, 5)

        self.colors = ['blue', 'red', 'yellow', 'cyan', 'magenta']

        self.item_id = self.canvas.create_oval(self.x_axis - self.R,
                                               self.y_axis - self.R,
                                               self.x_axis + self.R,
                                               self.y_axis + self.R,
                                               fill=choice(self.colors))

    def move(self):
        self.y_axis += self.speed
        self.canvas.move(self.item_id, 0, self.speed)

    def delete_target(self):
        self.canvas.delete(self.item_id)


def create_targets(canvas):
    global targets
    chance = randint(0, 20)
    if chance == 1:
        targets.append(Target(canvas))


def delete_targets(bullets, battlefield_events):
    for target in targets:
        if target.y_axis > 600:
            target.delete_target()
            targets.remove(target)
            battlefield_events.life_counting()
        for shell in bullets:
            for target in targets:
                distance = math.sqrt((target.x_axis - shell.x_axis) ** 2 + (target.y_axis - shell.y_axis) ** 2)
                if distance < target.R + shell.R:
                    shell.delete_bullet()
                    if shell in bullets:
                        bullets.remove(shell)
                    target.delete_target()
                    targets.remove(target)
                    battlefield_events.score_counting()


targets = []
