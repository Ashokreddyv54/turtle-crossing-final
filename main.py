import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    scoreboard.update_scoreboard()

#collide with car



    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.gameover()
            game_is_on=False
#Detect with boarder of other end
    if player.is_at_finishline():
        scoreboard.increase_score()
        player.start_position()
        car_manager.level_up()



screen.exitonclick()

