import random
import turtle
colors = ['red','cyan','pink' ,'yellow', 'green','orange']
t = turtle.Turtle()
t.speed(1000000)
turtle.bgcolor("black")
length=100
angle =50
size=5
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+20)
    t.pendown()
    t.left(20)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")                                                                    
