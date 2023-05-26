from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 0, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def final_score(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER!!! \n"
                   f"Score: {self.score}"
                   f"", align="center", font=("Arial", 0, "normal"))


