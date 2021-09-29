from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)