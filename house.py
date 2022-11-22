import turtle

def draw_triangle(tu, toa_do, canh, mau):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.fillcolor(mau)
    tu.begin_fill()
    tu.circle(-canh, steps = 3)
    tu.end_fill()

def draw_tecrangle(tu, toa_do, ngang, doc, mau):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.fillcolor(mau)
    tu.begin_fill()
    for i in range(2):
        tu.forward(ngang)
        tu.right(90)
        tu.forward(doc)
        tu.right(90)
    tu.end_fill()
               
def draw_trapezium(tu, toa_do,mau):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.fillcolor(mau)
    tu.begin_fill()
    tu.forward(30)
    tu.right(75)
    tu.forward(80)
    tu.right(105)
    tu.forward(71.42)
    tu.right(105)
    tu.forward(80)
    tu.end_fill()         
        
        
t = turtle.Turtle()
t.hideturtle()
t.speed(5)
t.pencolor("red")
turtle.bgcolor("lightskyblue")

#house
draw_tecrangle(t, (-120,40), 360, 160, "tan1")

draw_tecrangle(t, (-40,-30), 80, 90, "limegreen")

draw_tecrangle(t, (100,0), 100, 60, "white")


#roof
t.penup()
t.goto(-120, 40)
t.fillcolor("orangered3")
t.begin_fill()
t.goto(0, 160)
t.pendown()
t.goto(160, 40)
t.pendown()
t.goto(-120, 40)
t.penup()
t.goto(52, 120)
t.pendown()
t.goto(52, 200)
t.pendown()
t.goto(92, 200)
t.pendown()
t.goto(92, 90)
t.end_fill()

t.penup()
t.goto(62, 260)
t.pendown()
t.goto(62, 225)

t.penup()
t.goto(72, 275)
t.pendown()
t.goto(72, 220)

#tree
draw_triangle(t, (-260,-60), 40, "green")

draw_triangle(t, (-260,-20), 40, "green")

draw_triangle(t, (-260,20), 40, "green")

draw_trapezium(t, (-275, -120), "brown")








turtle.done()
    