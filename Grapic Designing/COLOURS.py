import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
color = ('violet','indigo','blue','green','yellow','orange','red')
for i in range (102):
    t.color(color[i%7])
    t.left(144)
    t.forward(i*2)
    t.rt(72)