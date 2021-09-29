from turtle import Turtle
import random

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color(random.choice(colors))
        new_seg.goto(position)
        self.segments.append(new_seg)

    def grow(self):
        self.add_segment(self.segments[-1].position())
    #     adds new seg to the end of the list


    def move(self):
        segments = self.segments
        # range(start=2, stop=0, step=-1)
        for seg_num in range(len(segments)-1, 0, -1):
            new_x = segments[seg_num-1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)