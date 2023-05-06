from turtle import Turtle

FONT = ('Comic Sans', 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("high_score.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.write_score()

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))

    def write_score(self):
        self.clear()
        self.goto(200, 250)
        self.write(f"Score is: {self.score}", move=False, align="center", font=FONT)
        self.goto(-170, 250)
        self.write(f"High_score is: {self.high_score}", move=False, align="center", font=FONT)

    def game_finish(self):
        self.goto(0, 0)
        self.write("CONGRATULATIONS!", align="center", font=('Comic Sans', 50, "normal"))
