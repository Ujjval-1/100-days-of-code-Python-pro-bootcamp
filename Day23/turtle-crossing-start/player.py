from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.moving = False

    def go_up(self):
        if self.moving:
            self.forward(MOVE_DISTANCE)
            self.getscreen().ontimer(self.go_up, 100)

    def start_moving(self):
        if not self.moving:
            self.moving = True
            self.go_up()

    def stop_moving(self):
        self.moving = False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >FINISH_LINE_Y:
            return True
        else:
            return False