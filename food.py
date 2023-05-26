from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        X = random.randint(-270, 270)
        Y = random.randint(-270, 270)
        self.goto(X, Y)
