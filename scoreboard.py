from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
