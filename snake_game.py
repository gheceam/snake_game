from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.screensize(600, 600, 'black')
# turns the screen tracer off so we can control when the screen refreshes
screen.tracer(0)

# create a Snake object
snake = Snake()
food = Food()
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
    time.sleep(.2)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.create_segment()
        food.refresh()

screen.exitonclick()
