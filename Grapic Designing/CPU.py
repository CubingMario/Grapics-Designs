import turtle
import colorsys

from Doraemon import ankur
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 500
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(2)
    t.forward(i*2)
    t.right(150)

if __name__ == '__main__':
    turtle.screensize(800, 600, "#f0f0f0")
    turtle.pensize(3)
    turtle.speed(9)
    ankur(100, -300)
    turtle.write('by Jeevesh', font=("Bradley Hand ITC", 30, "bold"))
    turtle.mainloop()