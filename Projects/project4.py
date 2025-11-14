#makes the turtle
import turtle


t = turtle.Turtle()
t.speed(10)
#stops drawing
t.penup()
t.goto(-150,-150)
t.color("purple")
t.pendown()
#Gives variation of colors
colors = ["red", "blue", "green"]
for i in range(10):
#Made the colors random
    t.color(colors[i % 3] )
    t.circle(30)
    t.forward(67)
    t.left(41)





turtle.exitonclick()
