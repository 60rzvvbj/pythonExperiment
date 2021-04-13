# 8．将第7题的代码改写为一个绘制五角星的函数
# 可以绘制指定边长和填充色的五角星。在画板上随机绘制若干五角星。
import turtle
import time
import random

turtle.hideturtle()
turtle.colormode(255)


def fun(length, color):
    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.speed(10)
    for i in range(0, 5):
        turtle.forward(length)
        turtle.right(180 - 36)
    turtle.end_fill()


for i in range(0, random.randint(40, 50)):
    fun(random.randint(50, 200), (random.randint(160, 220),
                                  random.randint(160, 220), random.randint(160, 220)))

turtle.done()
