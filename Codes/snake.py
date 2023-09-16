from turtle import Turtle
from time import sleep


class Snake:
    def __init__(self):
        self.head = Turtle(shape="square")
        self.head.color("white")
        self.head.penup()
        self.head.speed("fastest")
        self.body = [self.head]
        self.foods = 0

    def eat(self):
        for _ in range(self.foods - len(self.body) + 2):
            new_body_part = self.body[len(self.body) - 1].clone()
            new_body_part.back(20)
            self.body.append(new_body_part)

    def move(self):
        old_place = []
        old_heading = []
        for body_part in self.body:
            old_place.append(body_part.pos())
            old_heading.append(body_part.heading())
        self.body[0].forward(20)
        for body_part in self.body:
            if body_part == self.body[0]:
                pass
            else:
                body_part.setpos(old_place[self.body.index(body_part) - 1])
                body_part.setheading(old_heading[self.body.index(body_part) - 1])

    def go_up(self):
        if self.body[0].heading() != 270 and self.body[1].heading() != 270:
            self.body[0].setheading(90)

    def go_down(self):
        if self.body[0].heading() != 90 and self.body[1].heading() != 90:
            self.body[0].setheading(270)

    def go_right(self):
        if self.body[0].heading() != 180 and self.body[1].heading() != 180:
            self.body[0].setheading(0)

    def go_left(self):
        if self.body[0].heading() != 0 and self.body[1].heading() != 0:
            self.body[0].setheading(180)

    def wall_is_hit(self):
        for y in range(-300, 300):
            if self.body[0].distance(310, y) < 11 or self.body[0].distance(-310, y) < 11:
                return True

        for x in range(-300, 300):
            if self.body[0].distance(x, 310) < 11 or self.body[0].distance(x, -310) < 11:
                return True

    def is_alive(self):
        for part in self.body[2:]:
            if self.body[0].distance(part) < 10:
                self.reset()
        if self.wall_is_hit():
            self.reset()
        return True

    def reset(self):
        sleep(1)
        self.foods = 0
        self.head.goto(0, 0)
        self.head.setheading(0)
        if len(self.body) > self.foods + 1:
            for i in self.body:
                if i == self.body[0]:
                    pass
                else:
                    self.body.remove(i)
                    i.goto(1000, 1000)
