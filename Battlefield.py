class Battlefield:
    def __init__(self, canvas):
        self.canvas = canvas

        self.score = 0
        self.item_id = self.canvas.create_text(730, 570, text='Score: ' + str(self.score),
                                               font=("Helvetica", 20, 'bold'))

    def score_counting(self):
        self.score += 1
        self.canvas.itemconfig(self.item_id, text='Score: ' + str(self.score))
