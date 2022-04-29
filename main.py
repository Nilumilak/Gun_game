import tkinter as tk
import keyboard


class Character:
    def __init__(self):
        self.y = 550
        self.x = 300
        self.R = 50
        self.speed = 5
        self.jump_speed = 3
        self.max_jump_height = 10
        self.ground_position = int(self.max_jump_height * self.jump_speed)
        self.jump_position = self.max_jump_height * self.jump_speed
        self.character_id = canvas.create_oval(self.x - self.R, self.y - self.R,
                                               self.x + self.R, self.y + self.R,
                                               fill='black')

    def move(self):
        if keyboard.is_pressed('a'):
            if self.x > 2 + self.R:
                speed_back = -self.speed
                self.x += speed_back
                canvas.move(self.character_id, speed_back, 0)
        if keyboard.is_pressed('d'):
            if self.x < 800 - self.R:
                self.x += self.speed
                canvas.move(self.character_id, self.speed, 0)

    def jump(self):
        self.jump_position -= self.jump_speed
        canvas.move(self.character_id, 0, -self.jump_position)
        if self.jump_position <= -(self.ground_position - self.jump_speed):
            self.jump_position = self.ground_position


def frame():
    if keyboard.is_pressed('w'):
        ball.jump()
    ball.move()
    top.after(50, frame)


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')
canvas.pack()

ball = Character()
frame()

top.mainloop()
