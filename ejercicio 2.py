import turtle

t = turtle.Turtle()
t.pensize(6)
t.speed(2)
t.shape("arrow")

espacio = 20
lado = 100  

# --- FLECHA 1: Arriba · VERDE ---
t.penup()
t.goto(-50, -80)       
t.setheading(90)       
t.pendown()
t.color("green")
t.forward(lado)         
t.stamp()

# --- FLECHA 2: Derecha · NARANJA ---
t.penup()
t.goto(-50 + espacio, 50)  
t.setheading(0)            
t.pendown()
t.color("orange")
t.forward(lado)         
t.stamp()

# --- FLECHA 3: Abajo · ROJO ---
t.penup()
t.goto(90, 50 - espacio)   
t.setheading(270)          
t.pendown()
t.color("red")
t.forward(lado)            
t.stamp()

# -FLECHA 4: Izquierda · AZUL ---
t.penup()
t.goto(100 - espacio, -100)  
t.setheading(180)  
t.pendown()
t.color("blue")
t.forward(lado)            
t.stamp()

t.hideturtle()
turtle.done()
