import turtle
import math

print("=== CÍRCULO ===")
cx = float(input("x del centro: "))
cy = float(input("y del centro: "))
r = float(input("radio: "))

area = math.pi * r * r
print("Área =", round(area, 2))


t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(cx, cy - r)
t.pendown()
t.circle(r)

t.penup()
t.goto(cx, cy)
t.write(round(area, 2), align="center", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()
