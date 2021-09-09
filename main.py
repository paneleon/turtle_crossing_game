# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up.
#   On the next level, the car speed increases.
# 4. When the turtle collides with a car, it's game over and everything stops.

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
screen.onkey(turtle_player.go_up, "Up")

car_manager = CarManager()
car_manager.hideturtle()

# n = 0
game_is_on = True
while game_is_on:
    # n += 1
    time.sleep(0.1)
    screen.update()

    # creating a turle only on the sixth iteration before:
    # if n % 6 == 0:
    #     car_manager.create_car()
    # car_manager.move_car()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle_player.is_at_finish():
        turtle_player.go_to_start()
        car_manager.level_up()
        scoreboard.add_level()

screen.exitonclick()
