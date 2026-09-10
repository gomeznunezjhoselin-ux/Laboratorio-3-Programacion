import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)


# Triángulo azul
t.penup()
t.goto(-180, 30)
t.pendown()
t.color("black", "blue")
t.begin_fill()
t.goto(-160, 60)
t.goto(-140, 30)
t.goto(-180, 30)
t.end_fill()

# Cuadrado rojo
t.penup()
t.goto(-100, 30)
t.pendown()
t.color("black", "red")
t.begin_fill()
for _ in range(4):
    t.forward(35)
    t.left(90)
t.end_fill()

# Rectángulo amarillo
t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(35)
t.left(90)
t.forward(50)
t.left(90)
t.forward(35)
t.end_fill()

# Círculo verde
t.penup()
t.goto(60, 50)
t.pendown()
t.color("black", "green")
t.begin_fill()
t.circle(20)
t.end_fill()

# Rombo amarillo
t.penup()
t.goto(-170, -20)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.goto(-150, 5)
t.goto(-130, -20)
t.goto(-150, -45)
t.goto(-170, -20)
t.end_fill()

# Paralelogramo azul
t.penup()
t.goto(-90, -20)
t.pendown()
t.color("black", "blue")
t.begin_fill()
t.goto(-75, 0)
t.goto(-55, 0)
t.goto(-70, -20)
t.goto(-90, -20)
t.end_fill()

# Trapecio verde
t.penup()
t.goto(-10, -20)
t.pendown()
t.color("black", "green")
t.begin_fill()
t.goto(-25, 0)
t.goto(25, 0)
t.goto(10, -20)
t.goto(-10, -20)
t.end_fill()

# Óvalo acostado rojo
t.penup()
t.goto(60, 0)
t.pendown()
t.color("black", "red")
t.begin_fill()
for _ in range(2):
    t.circle(25, 90)
    t.circle(12, 90)
t.end_fill()

t.hideturtle()
turtle.done()
