import turtle

# Setup
turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)

# Curve drawing function
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

# Heart drawing
turtle.color('red', 'pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

# Write name/message inside heart
turtle.penup()
turtle.goto(0, 30)  # Adjust this position if needed
turtle.color('white')
turtle.write("Muskan Rajput", align="center", font=("Arial", 18, "bold"))

turtle.done()
