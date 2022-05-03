from random import randint, choice


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


def delete_targets(canvas, bullets):
    for target in targets:
        if target.y_axis > 600:
            target.delete_target()
            canvas.delete(target)
            targets.remove(target)
        for shell in bullets:
            for target in targets:
                if (target.x_axis - target.R < shell.x_axis < target.x_axis + target.R
                        and target.y_axis - target.R < shell.y_axis < target.y_axis + target.R):
                    shell.delete_bullet()
                    canvas.delete(shell)
                    if shell in bullets:
                        bullets.remove(shell)
                    target.delete_target()
                    canvas.delete(target)
                    targets.remove(target)


targets = []
