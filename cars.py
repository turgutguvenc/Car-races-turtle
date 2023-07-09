from turtle import Turtle, colormode
from random import randint

colormode(255)
SPEED = 5
INCREASE_SPEED = 5


class Car:
    """
    This class represents a car in the game.

    Attributes:
        all_cars (list): A list to store all the car objects.
        speed (int): The initial speed of the cars.

    Methods:
        create_car(): Create a new car and add it to the all_cars list.
        colors_(): Generate a random RGB color tuple.
        move(): Move the cars backward by the current speed.
        make_fast(): Increase the speed of the cars.
    """

    def __init__(self):
        """
        Initializes a new instance of the Car class.
        """
        self.all_cars = []
        self.speed = SPEED

    def create_car(self):
        """
        Create a new car and add it to the all_cars list.
        """
        random_choice = randint(1, 6)
        if random_choice == 1:
            car = Turtle()
            car.shape("square")
            car.color(self.colors_())
            car.shapesize(stretch_wid=1, stretch_len=1.5)
            car.penup()
            random_y = randint(-290, 290)
            car.goto(x=290, y=random_y)
            self.all_cars.append(car)

    def colors_(self):
        """
        Generate a random RGB color tuple.
        """
        return (randint(0, 255),
                randint(0, 255),
                randint(0, 255))

    def move(self):
        """
        Move the cars backward by the current speed.
        """
        for car in self.all_cars:
            car.backward(self.speed)

    def make_fast(self):
        """
        Increase the speed of the cars.
        """
        self.speed += INCREASE_SPEED