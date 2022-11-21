import turtle



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
               
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("blue")


draw_tecrangle(t, (-90,150), 90, 150, "pink")
draw_tecrangle(t, (-60,100), 30, 50, "white")

draw_tecrangle(t, (0,150), 90, 150, "pink")
draw_tecrangle(t, (30,100), 30, 50, "white")

draw_tecrangle(t, (-90,0), 90, 150, "pink")
draw_tecrangle(t, (-60,-50), 30, 50, "white")

draw_tecrangle(t, (0,0), 90, 150, "pink")
draw_tecrangle(t, (30,-50), 30, 50, "white")

draw_tecrangle(t, (90,0), 180, 150, "lightblue3")
draw_tecrangle(t, (150,-75), 30, 75, "lightseagreen")
draw_tecrangle(t, (180,-75), 30, 75, "lightseagreen")

turtle.done()
    