import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
scoreboard = Scoreboard()

screen.listen()
# moves turtle up when the "up" key is pressed
screen.onkey(turtle_player.go_up, "Up")

car_manager = CarManager()
car_manager.hideturtle()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # randomly generates cars along the Y-coordinates
    car_manager.create_car()
    #  and moves cars from right to left edges of screen
    car_manager.move_car()

    for car in car_manager.all_cars:
        # detects hit by a car
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detects successful crossing, moves the turtle back and levels up
    if turtle_player.is_at_finish():
        turtle_player.go_to_start()
        car_manager.level_up()
        scoreboard.add_level()

screen.exitonclick()
