import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.screensize(600, 600, 'black')
# turns the screen tracer off so we can control when the screen refreshes
screen.tracer(0)

# create a Snake object
snake = Snake()
food = Food()
score_board = Scoreboard(screen)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# indicate that the game is still running
game_is_on = True

# while the game is on the snake will continue to move
while game_is_on:
    # only update the screen refresh once all the segments moved
    screen.update()
    # use a slight delay between movements to slow down the motion
    time.sleep(.08)
    collided = snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.create_segment()
        score_board.update_score()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 495 or snake.head.xcor() < -495 \
            or snake.head.ycor() > 400 or snake.head.ycor() < -400 or collided is True:
        gameover = Turtle()
        gameover.color("white")
        gameover.hideturtle()
        gameover.write("Game Over!", False, "center", ("Courier", 18, "normal"))
        game_is_on = False

screen.exitonclick()
