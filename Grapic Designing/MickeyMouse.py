import turtle
mm = turtle.Turtle()
mm.speed(0)

bg = mm.getscreen()
bg.bgcolor('White')

#head
mm.begin_fill()
mm.color('black')
mm.circle(100)
mm.end_fill()

#left ear
mm.goto(-80,140)
mm.begin_fill()
mm.color('black')
mm.circle(60)
mm.end_fill()

#right ear
mm.goto(80,140)
mm.begin_fill()
mm.color('black')
mm.circle(60)
mm.end_fill()

#face dip
mm.goto(4,-4)
mm.begin_fill()
mm.color('BlanchedAlmond')
mm.circle(80)
mm.end_fill()

mm.goto(-4,-4)
mm.begin_fill()
mm.color('BlanchedAlmond')
mm.circle(80)
mm.end_fill()


#face outline
mm.goto(0,0)
mm.color('black')
mm.circle(100)

#left eye
mm.penup()
mm.goto(-50,70)
mm.pendown()
mm.begin_fill()
mm.color('White')
mm.circle(30)
mm.end_fill()

mm.penup()
mm.goto(-50,80)
mm.pendown()
mm.begin_fill()
mm.color('black')
mm.circle(10)
mm.end_fill()

# right eye
mm.penup()
mm.goto(50,70)
mm.pendown()
mm.begin_fill()
mm.color('White')
mm.circle(30)
mm.end_fill()

mm.penup()
mm.goto(50,80)
mm.pendown()
mm.begin_fill()
mm.color('black')
mm.circle(10)
mm.end_fill()

#nose
mm.penup()
mm.goto(0,50)
mm.pendown()
mm.begin_fill()
mm.color('Black')
mm.circle(5)                              
mm.end_fill()

mm.penup()
mm.goto(2,50)
mm.pendown()
mm.begin_fill()
mm.color('White')
mm.circle(2)                              
mm.end_fill()

mm.speed(3)
#lips
mm.penup()
mm.goto(-50,40)
mm.pendown()
mm.right(90)
mm.setheading(-60)
mm.begin_fill()
mm.color('Pink')
for x in range (130):
    mm.forward(1)
    mm.left(1)
mm.left(115)
mm.forward(110)
mm.end_fill()

