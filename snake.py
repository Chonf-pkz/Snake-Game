from turtle import Turtle
location = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.ok = []
        self.create_snake()
        self.head = self.ok[0]

    def create_snake(self):
         for a_turtle in location:
            self.add_segment(a_turtle)

    def add_segment(self, a_turtle):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(a_turtle)
        self.ok.append(new_turtle)

    def grow(self):
        last_segment = self.ok[-1]
        new_x = last_segment.xcor()
        new_y = last_segment.ycor()
        self.add_segment((new_x, new_y))

    def move(self):
        for b in range(len(self.ok) - 1, 0, -1):
            new_x = self.ok[b - 1].xcor()
            new_y = self.ok[b - 1].ycor()
            self.ok[b].goto(new_x, new_y)
        self.ok[0].forward(20)

    def turn_right(self):
        self.head.setheading(0)

    def turn_left(self):
        self.head.setheading(180)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.ok[0].setheading(270)


