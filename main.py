import time
from turtle import Turtle, Screen, colormode
from cars import Car
from racer import Player
from scoreboard import ScoreBoard
from random import randint

colormode(255)
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = ScoreBoard()
screen.listen()

# Player controls
screen.onkey(player.move, "w")

car = Car()

game_is_on = True
while game_is_on:

    # Create a new car
    car.create_car()

    # Move the cars
    car.move()

    # Pause for a short period
    time.sleep(0.1)

    # Detect collision with car
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful pass
    if player.ycor() > 285:
        score.increase_level()
        player.restart()
        car.make_fast()

    # Update the screen
    screen.update()

# Exit the game when the screen is clicked
screen.exitonclick()