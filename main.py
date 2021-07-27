import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player_turtle = Player()

screen.listen()
screen.onkeypress(player_turtle.move_forward, "Up")

scoreboard_game = Scoreboard()
car_manager_game = CarManager()

game_is_on = True
i=0
while game_is_on:
    time.sleep(0.1)
    if i % 5 == 0:
        car_manager_game.include_new_car()
    car_manager_game.move_cars()
    screen.update()
    if player_turtle.ycor() > player.FINISH_LINE_Y:
        scoreboard_game.increase_level()
        player_turtle.starting_position()
        car_manager_game.increment_level()
    if car_manager_game.detect_collision(player_turtle):
        game_is_on = False
        scoreboard_game.game_over()
    i+=1


screen.exitonclick()
