import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreborad import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = Snake()
food = Food()
score = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")


is_on = True

while is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.grow()
        score.increase_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        score.reset()
        my_snake.reset()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            is_on = False
            score.reset()
            my_snake.reset()


my_screen.exitonclick()
