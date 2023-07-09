from turtle import Turtle

ALINGMENT = "left"
FONT: tuple[str, int, str] = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    """
    This class represents the scoreboard in the game.

    Attributes:
        level (int): Represents the player's level.

    Methods:
        __init__(): Initializes a new instance of the ScoreBoard class.
        update_scoreboard(): Update the scoreboard with the current scores.
        point(): Increment the player's score by 1 and update the scoreboard.
        game_over(): Display the "GAME OVER" message on the screen.
    """

    def __init__(self):
        """
        Initializes a new instance of the ScoreBoard class.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current scores.
        """
        self.clear()
        self.goto(x=-50, y=270)
        self.write(align=ALINGMENT, arg=f"Level: {self.level}", font=FONT)

    def increase_level(self):
        """
        Increment the player's level by 1 and update the scoreboard.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Display the "GAME OVER" message on the screen.
        """
        self.goto(0, 0)
        self.write('GAME OVER', align=ALINGMENT, font=FONT)