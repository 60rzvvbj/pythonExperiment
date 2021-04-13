# 7．使用turtle库绘制一个五角星图案。
import turtle
import time
turtle.hideturtle()
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('#f00')
turtle.fillcolor('#f00')
turtle.begin_fill()
turtle.speed(5)
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(180 - 36)
turtle.end_fill()
turtle.done()
