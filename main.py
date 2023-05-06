from turtle import Screen
import turtle
from judet_manager import County
from time import sleep
import pandas
from score import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=700, height=600)
    screen.bgpic("Romania.gif")
    screen.tracer(0)

    data = pandas.read_csv("judete.csv")
    counties_list = data.county.to_list()
    data_list = data.to_dict()
    print(data_list)
    already_guessed = []
    score = Scoreboard()

    # screen.listen()
    # screen.onkeypress(key="Up", fun=arad.move_up)
    # screen.onkeypress(key='Down', fun=arad.move_down)
    # screen.onkeypress(key='Right', fun=arad.move_right)
    # screen.onkeypress(key='Left', fun=arad.move_left)


    while True:
        sleep(0.1)
        screen.update()
        guess = screen.textinput("Make a guess", "Ghicește un județ")
        if guess.title() in counties_list:
            if guess.title() in already_guessed:
                print("Already Guessed")
                continue
            print("All good")
            new_judet = County()
            already_guessed.append(guess.title())
            score.increase_score()
            score.write_score()
        else:
            print("nope")

    screen.exitonclick()
