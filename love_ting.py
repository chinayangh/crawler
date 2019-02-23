# -*- coding: utf-8 -*-

import turtle
turtle.color('gold', 'pink')
#笔粗细
turtle.pensize(7)
#速度
turtle.speed(20)
def zxt(a, b, c,d):
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.left(c)
    for i in range(d):
        turtle.forward(2)

#张
#弓字旁
zxt(-200,250,0,20)
zxt(-160,250,-90,20)
zxt(-200,210,90,20)
zxt(-200,210,-90,20)
zxt(-200,170,90,20)
zxt(-160,170,-90,20)
zxt(-200,130,90,20)
#长
zxt(-150,200,0,25)
zxt(-140,250,-90,60)
zxt(-140,130,120,10)
zxt(-100,230,-180,20)
zxt(-130,200,90,25)
#日字
turtle.color( 'violet')
# 笔粗细
turtle.pensize(7)
# 速度
turtle.speed(20)
zxt(-60,210,-30,30)
zxt(-60,210,90,15)
zxt(-30,210,-90,30)
zxt(-60,180,90,15)
zxt(-60,150,0,15)
#尧字
#turtle.color('red')
# 笔粗细
turtle.pensize(7)
# 速度
turtle.speed(20)
zxt(30,250,-160,30)
zxt(-10,250,100,30)
zxt(25,200,80,10)
zxt(35,230,-170,25)
zxt(-15,180,152,30)
zxt(15,180,-120,30)
zxt(-18,125,-50,10)
zxt(20,180,78,30)
zxt(20,120,90,20)
zxt(60,120,90,10)
#女
turtle.color('pink')
zxt(120,250,160,35)
zxt(100,180,70,35)
zxt(150,210,-75,50)
zxt(80,200,115,35)
#亭
zxt(190,250,-25,5)
zxt(160,240,25,40)
zxt(175,230,-90,10)
zxt(175,230,90,25)
zxt(225,230,-90,10)
zxt(175,210,90,25)
zxt(165,200,-90,5)
zxt(165,200,90,35)
zxt(235,200,-90,5)
zxt(200,180,0,30)
zxt(200,120,-120,5)
zxt(175,180,-150,25)
#画心
def LittleHeart():
            for i in range(200):
                turtle.right(1)
                turtle.forward(2)
# 窗口大小# 颜色
turtle.color('red', 'pink')
# 笔粗细
turtle.pensize(3)
# 速度
turtle.speed(5)
# 提笔
turtle.up()
# 隐藏笔
turtle.hideturtle()
# 去到的坐标,窗口中心为0,0
turtle.goto(0, -220)
turtle.showturtle()
# 画上线
turtle.down()
turtle.speed(5)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
# 调用画爱心左边的顶部
LittleHeart()
#  调用画爱右边的顶部
turtle.left(120)
LittleHeart()
# 画下线
turtle.speed(10)
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.showturtle()
#第一句话
turtle.speed(1)
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('LightSalmon', 'pink')
turtle.write("因为我刚好遇见你", font=('algerian', 30,), align="center")
turtle.up()
turtle.showturtle()

window = turtle.Screen()
window.exitonclick()
#turtle.done()
