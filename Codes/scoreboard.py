from turtle import Turtle
FONT = ("Times New Roman", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)

    def show_score(self):
        self.clear()
        data_as_txt = open("data.txt", mode="r")
        data = data_as_txt.read()
        data_as_txt.close()
        highest_score = int(data.split(" ")[0])
        self.write(f"Score: {self.score}  Highest Score: {highest_score}", move=False, align="center", font=FONT)
        if self.score > highest_score:
            data_as_txt = open("data.txt", mode="w")
            data_as_txt.write(f"{self.score}")
            data_as_txt.close()
