from turtle import Turtle


FONT = ('Comic Sans', 12, "normal")
FONT_SMALL = ('Comic Sans', 5, "normal")


class County(Turtle):

    def __init__(self, position, name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.name = name
        if len(self.name) < 9:
            self.write(self.name, move=False, align="center", font=FONT)
        else:
            self.write(self.name, move=False, align="center", font=FONT_SMALL)


