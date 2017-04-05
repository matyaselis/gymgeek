import turtle

size = 250
turtle.shape("turtle")
turtle.color(255/255, 135/255, 255/255)
turtle.pensize(10)
for _ in range(3):
    for _ in range(4):     
        turtle.forward(size)
        turtle.left(90)

    turtle.right(50)
  
