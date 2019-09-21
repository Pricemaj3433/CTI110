# This program will create a graphic using turtle
# Date- 9/20/2019
# CTI-110 P2HW2 - Turtle Graphic
# Jeffrey Price-Maupin

#create a triangle 
#fill the triangle with color
#create a 2nd triangle around the first

import turtle
turtle.hideturtle()
turtle.goto(-100, -100)
turtle.begin_fill()
turtle.forward(200)
turtle.goto(0,0)
turtle.end_fill()
turtle.goto(-100, -100)
turtle.goto(0, 100)
turtle.goto(100, -100)
turtle.showturtle
