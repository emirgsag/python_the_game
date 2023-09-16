from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Go Eat Yourself")

scoreboard = Scoreboard()

pen = Turtle()
pen.hideturtle()
pen.pencolor("White")

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(fun=snake.go_up, key="w")
screen.onkeypress(fun=snake.go_down, key="s")
screen.onkeypress(fun=snake.go_right, key="d")
screen.onkeypress(fun=snake.go_left, key="a")

while snake.is_alive():
    screen.tracer(0)
    scoreboard.show_score()
    snake.move()
    food.get_food()
    if food.foods[0].distance(snake.body[0]) < 15:
        food.foods.remove(food.foods[0])
        snake.foods += 1
    scoreboard.score = snake.foods
    snake.eat()
    screen.update()
    time.sleep(0.1)

# screen.clearscreen()
# screen.bgcolor("Black")
# result = f'''      Game over!!!
# You\'ve eaten {snake.foods} foods.'''
# pen.write(result, move=False, align="center", font=("Times New Roman", 20, "normal"))
screen.exitonclick()
