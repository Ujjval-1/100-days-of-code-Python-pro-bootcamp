from turtle import Turtle

from anyio import sleep

starting_pos = [(0, 0), (-20,0), (-40,0)]
move_dist = 20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        for position in starting_pos:
            self.add_segment(position)

    def add_segment(self,position):
        sq = Turtle(shape="square")
        sq.color("white")
        sq.penup()
        sq.goto(position)
        self.segments.append(sq)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
