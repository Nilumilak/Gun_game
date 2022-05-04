import tkinter as tk


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

    def score_counting(self):
        self.score += 1
        self.canvas.itemconfig(self.score_item_id, text='Score: ' + str(self.score))

    def life_counting(self):
        self.life_numbers -= 1
        self.canvas.itemconfig(self.life_item_id, text=self.life_text * self.life_numbers)
