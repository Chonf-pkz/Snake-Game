from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.pendown()
        self.update_point()

    def update_point(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 12, "normal"))

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("FONT", 28, "normal"))

    def got_point(self):
        self.score += 1
        self.update_point()