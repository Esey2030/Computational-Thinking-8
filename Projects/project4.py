
import turtle


t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-150,-150)
t.color("purple")
t.pendown()
colors = ["red", "blue", "green"]
for i in range(10):
    t.color(colors[i % 3] )
    t.circle(30)
    t.forward(67)
    t.left(41)





turtle.exitonclick()
