import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
foods = Food()
screen.listen()
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
score = Score()
a = True
while a:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(foods) < 15:
        foods.refresh()
        score.got_point()
        snake.grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        a = False
        score.game_over()
    for segment in snake.ok[1:]:  # Bỏ qua đầu rắn (self.ok[0])
        if snake.head.distance(segment) < 10:
            a = False  # Dừng game
            score.game_over()



screen.exitonclick()