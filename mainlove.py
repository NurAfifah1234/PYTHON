from turtle import *
getscreen()
bgcolor("white")
pencolor("lightblue")
pensize(15)

fillcolor("blue")
begin_fill()
speed(2)
left(140)
forward(180)
circle(-90, 200)
left(120)
circle(-90, 200)
forward(180)

shape("circle")
end_fill()

penup()
goto(0, -100)
color("black")
write("love", align="center", font=("calibri", 16, "bold"))

hideturtle()
done()