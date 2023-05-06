from turtle import Turtle


FONT = ('Comic Sans', 12, "normal")
FONT_SMALL = ('Comic Sans', 5, "normal")

class Writer(Turtle):

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

    def move_left(self):
        self.setx(self.xcor() - 10)
        self.clear()
        if len(self.name) < 9:
            self.write(self.name, move=False, align="center", font=FONT)
        else:
            self.write(self.name, move=False, align="center", font=FONT_SMALL)
        print((self.xcor(), self.ycor()))

    def move_right(self):
        self.setx(self.xcor() + 10)
        self.clear()
        if len(self.name) < 9:
            self.write(self.name, move=False, align="center", font=FONT)
        else:
            self.write(self.name, move=False, align="center", font=FONT_SMALL)
        print((self.xcor(), self.ycor()))

    def move_up(self):
        self.sety(self.ycor() + 10)
        self.clear()
        if len(self.name) < 9:
            self.write(self.name, move=False, align="center", font=FONT)
        else:
            self.write(self.name, move=False, align="center", font=FONT_SMALL)
        print((self.xcor(), self.ycor()))

    def move_down(self):
        self.sety(self.ycor() - 10)
        self.clear()
        if len(self.name) < 9:
            self.write(self.name, move=False, align="center", font=FONT)
        else:
            self.write(self.name, move=False, align="center", font=FONT_SMALL)
        print((self.xcor(), self.ycor()))
