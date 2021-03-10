from turtle import Turtle
import random
import time


class Food(Turtle) :

    def __init__(self) :
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh(0)

    def refresh(self, wait) :
        random_x = random.randint(-550, 550)
        random_y = random.randint(-350, 350)
        self.goto(random_x, random_y)
