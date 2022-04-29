import tkinter as tk


class Character:
    def __init__(self):
        self.y = 500
        self.x = 300
        self.R = 100
        canvas.create_oval(self.x, self.y, self.x + self.R, self.y + self.R, fill='black')

    def move(self):
        pass


top = tk.Tk()
top.title('Ball game')
canvas = tk.Canvas(top, width=800, height=600, bg='white')

canvas.pack()
ball = Character()

top.mainloop()
