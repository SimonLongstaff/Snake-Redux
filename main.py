from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random
import threading

# Screen set up
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Game Start
game_active = True

# Game set up
snake = Snake()
food = Food()
bonus = Food()
extra = Food()
extra.color("yellow")
bonus.color("red")
scoreboard = Scoreboard()

# Control listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def game_over() :
    scoreboard.reset_scoreboard()
    snake.reset_snake()


while game_active :

    # Game speed Controls
    speed = 0.1 / 1 - ((scoreboard.getscore() / 1000) + (scoreboard.getbonus() / 1000))
    screen.update()
    time.sleep(speed)

    # Randomly spawn and move bonus and extra food
    ran = random.randint(0, 1000)

    if ran <= 5 :
        bonus.showturtle()
        bonus.refresh(0)

    if ran >= 995 :
        extra.showturtle()
        extra.refresh(0)

    # Food Collision
    if snake.head.distance(food) < 20 :
        food.refresh(0)
        scoreboard.increase_score(1, 1, 0)
        snake.extend()

    # Extra Collision
    if snake.head.distance(extra) < 20 and extra.isvisible() :
        extra.hideturtle()
        scoreboard.increase_score(1, -45, -2)
        for i in range(10) :
            snake.extend()

    # Bonus Collision
    if snake.head.distance(bonus) < 20 and bonus.isvisible() :
        bonus.hideturtle()
        scoreboard.increase_score(0, 5, 5)
        if len(snake.segments) > 8 :
            for seg_num in range(len(snake.segments) - 1, len(snake.segments) - 6, -1) :
                snake.change_colour(seg_num)
            for seg_num in range(len(snake.segments) - 1, len(snake.segments) - 6, -1) :
                scoreboard.increase_score(1, 1, 0)
                snake.destroy_tail(seg_num)

    # Wall Collision
    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 380 or snake.head.ycor() < -380 :
        game_over()

    # Tail Collsion
    for segment in snake.segments[1 :] :
        if snake.head.distance(segment) < 10 :
            game_over()

    snake.move()

screen.exitonclick()
