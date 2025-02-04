import turtle
import turtle as t
import random
from turtle import Screen

import colorgram

rgb_colors = []
colors = colorgram.extract('hirst_dot_painting.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    a = r,g,b
    rgb_colors.append(a)
print(rgb_colors)

turtle.colormode(255)
turtle1 = t.Turtle()
turtle1.speed('fastest')
turtle1.penup()
turtle1.hideturtle()
extracted_color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)
dots = 100

for dot_count in range(1,dots+1):
    turtle1.dot(20,random.choice(extracted_color_list))
    turtle1.forward(50)

    if dot_count%10==0:
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)


screen = Screen()
screen.exitonclick()