from turtle import Screen
import turtle
from judet_manager import Writer
from time import sleep

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=700, height=600)
    screen.bgpic("Romania.gif")
    screen.tracer(0)

    arad = Writer((120, -88), "Vaslui")

    screen.listen()
    screen.onkeypress(key="Up", fun=arad.move_up)
    screen.onkeypress(key='Down', fun=arad.move_down)
    screen.onkeypress(key='Right', fun=arad.move_right)
    screen.onkeypress(key='Left', fun=arad.move_left)


    while True:
        sleep(0.1)
        screen.update()

    screen.exitonclick()
