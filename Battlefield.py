import tkinter as tk
import Bullet


class Battlefield:
    def __init__(self, canvas):
        self.canvas = canvas

        self.score = 0
        self.score_item_id = self.canvas.create_text(650, 570, text='Score: ' + str(self.score),
                                                     font=("Helvetica", 20, 'bold'), anchor=tk.SW)

        self.life_text = '♥ '
        self.life_numbers = 3
        self.life_item_id = self.canvas.create_text(650, 530, text=self.life_text * self.life_numbers,
                                                    font=("Helvetica", 30), fill='red', anchor=tk.SW)

        self.bullet_item_id = self.canvas.create_text(650, 480, text='Bullets: ' + str(Bullet.bullet_amount),
                                                    font=("Helvetica", 20, 'bold'), anchor=tk.SW)

    def score_counting(self):
        self.score += 1
        self.canvas.itemconfig(self.score_item_id, text='Score: ' + str(self.score))
        if self.score % 50 == 0:
            self.add_bullet()

    def life_counting(self):
        self.life_numbers -= 1
        self.canvas.itemconfig(self.life_item_id, text=self.life_text * self.life_numbers)

    def add_lifes(self):
        if self.life_numbers < 4:
            self.life_numbers += 1
            self.canvas.itemconfig(self.life_item_id, text=self.life_text * self.life_numbers)

    def bullet_counting(self):
        Bullet.bullet_amount -= 1
        self.canvas.itemconfig(self.bullet_item_id, text='Bullets: ' + str(Bullet.bullet_amount))

    def add_bullet(self):
        Bullet.bullet_amount += 1
        self.canvas.itemconfig(self.bullet_item_id, text='Bullets: ' + str(Bullet.bullet_amount))
