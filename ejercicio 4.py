import turtle

t = turtle.Turtle()
t.pensize(10)
t.color("darkgreen")
t.speed(2)

# ====== LETRA J ======
t.penup()           
t.goto(-60, 80)   
t.pendown()         

t.right(90)
t.forward(200)     
t.right(90)
t.forward(50)       
t.right(90)
t.forward(50)       

t.penup()
t.home()            
t.color("darkred")

# ==== LETRA G ====
t.penup()
t.goto(50, 80)      
t.pendown()

t.forward(-50)       
t.right(90)
t.forward(200)      
t.right(90)
t.forward(-50)       
t.right(90)
t.forward(75)      
t.left(90)
t.forward(15)       

t.hideturtle()
turtle.done()
