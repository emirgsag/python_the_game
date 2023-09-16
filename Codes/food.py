from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("red")
        self.food.penup()
        self.food.shapesize(0.5, 0.5)
        self.food.setpos(random.randint(-280, 280), random.randint(-280, 280))
        self.foods = [self.food]

    def get_food(self):
        if len(self.foods) == 0:
            self.food.hideturtle()
            self.food.setpos(random.randint(-280, 280), random.randint(-280, 280))
            self.food.showturtle()
            self.foods.append(self.food)
