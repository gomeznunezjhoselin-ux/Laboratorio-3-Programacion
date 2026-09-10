import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("skyblue")

def rect(x, y, w, h, c):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c, c)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# Sol
t.penup()
t.goto(-300, 180)
t.pendown()
t.color("yellow", "yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# Nubes
def cloud(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white", "white")
    t.begin_fill()
    t.circle(20)
    t.goto(x+25, y+10)
    t.circle(25)
    t.goto(x+50, y)
    t.circle(20)
    t.end_fill()
cloud(-180, 170)
cloud(50, 190)

# Montañas
t.penup()
t.goto(-400, 0)
t.pendown()
t.color("saddlebrown", "saddlebrown")
t.begin_fill()
t.goto(-280, 120)
t.goto(-150, 0)
t.goto(0, 150)
t.goto(150, 30)
t.goto(300, 100)
t.goto(400, -20)
t.goto(-400, -20)
t.end_fill()

# Pasto
rect(-400, -80, 800, 150, "forestgreen")

# Lago
t.penup()
t.goto(-300, -30)
t.pendown()
t.color("cyan", "cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

# Árbol
rect(-200, -50, 15, 60, "saddlebrown")
t.penup()
t.goto(-192, 10)
t.pendown()
t.color("darkgreen", "darkgreen")
t.begin_fill()
t.circle(35)
t.end_fill()

# Casa
rect(50, -50, 100, 80, "peachpuff")
t.penup()
t.goto(40, 30)
t.pendown()
t.color("darkred", "firebrick")
t.begin_fill()
t.goto(100, 80)
t.goto(160, 30)
t.goto(40, 30)
t.end_fill()
rect(85, -50, 30, 45, "saddlebrown")
rect(115, 0, 20, 20, "lightblue")

# Calle
rect(-400, -130, 800, 50, "dimgray")

# Auto
rect(-250, -130, 60, 25, "red")
for r in [(-235, -135), (-205, -135)]:
    t.penup()
    t.goto(r)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

# Autobús
rect(-50, -140, 120, 35, "purple")
for r in [(-30, -145), (40, -145)]:
    t.penup()
    t.goto(r)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Semáforo
rect(250, -50, 10, 90, "gray")
rect(240, -20, 30, 60, "black")
t.penup()
t.goto(255, 30)
t.dot(15, "red")
t.goto(255, 10)
t.dot(15, "yellow")
t.goto(255, -10)
t.dot(15, "green")

t.hideturtle()
turtle.done()
