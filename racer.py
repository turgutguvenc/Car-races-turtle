from turtle import Turtle, colormode

MOVE_DISTANCE = 10
colormode(255)
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    This class represents a player in the game.

    Attributes:
        MOVE_DISTANCE (int): The distance the player moves vertically with each movement.
        STARTING_POSITION (tuple): The starting position of the player on the screen.
        FINISH_LINE_Y (int): The y-coordinate of the finish line.

    Methods:
        __init__(): Initializes a new instance of the Player class.
        move(): Move the player vertically by the MOVE_DISTANCE value.
        restart(): Reset the player's position to the starting position.
    """

    def __init__(self):
        """
        Initializes a new instance of the Player class.
        """
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.restart()

    def move(self):
        """
        Move the player vertically by the MOVE_DISTANCE value.
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def restart(self):
        """
        Reset the player's position to the starting position.
        """
        self.goto(STARTING_POSITION)
