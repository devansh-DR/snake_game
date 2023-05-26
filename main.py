from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

score = 0
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.final_score()
        game_on = False

    # detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.final_score()
            game_on = False


screen.exitonclick()
