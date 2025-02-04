from turtle import Turtle,Screen

turtle1 =Turtle()
screen = Screen()

def forward():
    turtle1.forward(10)

def back():
    turtle1.backward(10)

def turn_left():
    turtle1.left(10)

def turn_right():
    turtle1.right(10)

def clear():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")



screen.exitonclick()