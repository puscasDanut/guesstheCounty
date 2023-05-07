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
    already_guessed = []
    missing_counties_list = []
    score = Scoreboard()

    while len(already_guessed) < 42 and score.score < 42:
        sleep(0.1)
        screen.update()
        guess = screen.textinput("Make a guess", "Ghicește un județ")
        if guess.title() == "Exit":
            break
        if guess.title() in counties_list:
            if guess.title() in already_guessed:
                continue
            new_judet_xcor = int((data[data.county == guess.title()]["x"]))
            new_judet_ycor = int((data[data.county == guess.title()]["y"]))
            new_judet_cords = (new_judet_xcor, new_judet_ycor)
            new_judet = County(new_judet_cords, guess.title())
            already_guessed.append(guess.title())
            score.increase_score()
            score.write_score()

    for county in counties_list:
        if county not in already_guessed:
            missing_counties_list.append(county)
    missing_counties = pandas.DataFrame(missing_counties_list)
    missing_counties.to_csv("missing_judete.csv")

    screen.clear()
    screen.bgpic("Romania.gif")
    score.game_finish()
    screen.exitonclick()
