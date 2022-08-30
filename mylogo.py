import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.title("mylogo")
turtle.pencolor("red")
turtle.pensize(5)
turtle.right(-45) 
turtle.forward(-100)
turtle.right(-45)

turtle.circle(70.710,90)
turtle.pencolor("black")
turtle.circle(70.710,180)
turtle.pencolor("red")
turtle.circle(70.710,90)

turtle.left(-135) #左转弯和右转弯一个意思不用写
turtle.pencolor("red")
turtle.forward(100)
turtle.left(90) #左转弯和右转弯一个意思不用写
turtle.pencolor("black")
turtle.forward(100)
turtle.done()  
