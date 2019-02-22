# -*- coding: utf-8 -*-

import turtle
turtle.color('gold', 'pink')
#笔粗细
turtle.pensize(7)
#速度
turtle.speed(100)
def zwj(a, b, c,d):
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.left(c)
    for i in range(d):
        turtle.forward(2)




#程
#禾字旁
zwj(-210,250,30,35)
zwj(-220,220,-29,40)
zwj(-180,260,-90,66)
zwj(-180,200,-50,30)
zwj(-180,200,100,30)
#口
zwj(-110,280,-50,15)
zwj(-110,280,90,15)
zwj(-75,280,-90,15)
zwj(-75,250,-90,15)
#王字
turtle.color( 'violet')
# 笔粗细
turtle.pensize(7)
# 速度
turtle.speed(100)
zwj(-130,220,180,40)
zwj(-120,180,0,30)
zwj(-130,150,0,40)
zwj(-90,220,-90,35)
#珊字
turtle.color('SpringGreen')
# 笔粗细
turtle.pensize(7)
# 速度
turtle.speed(100)
#王
zwj(-30,220,90,20)
zwj(-30,180,0,20)
zwj(-30,150,0,20)
zwj(-15,220,-90,35)
#册
zwj(30,270,-2,80)
zwj(30,270,90,10)
zwj(50,270,-90,80)
zwj(70,270,-2,80)
zwj(70,270,90,10)
zwj(90,270,-90,80)
zwj(15,200,90,40)
#王
zwj(100,220,0,20)
zwj(100,180,0,20)
zwj(100,150,0,20)
zwj(120,220,-90,35)
#册
zwj(160,270,0,80)
zwj(160,270,90,10)
zwj(180,270,-90,80)
zwj(200,270,0,80)
zwj(200,270,90,10)
zwj(220,270,-90,80)
zwj(150,200,90,40)
#画心
def LittleHeart():
            for i in range(205):
                turtle.right(1)
                turtle.forward(2)
# 窗口大小# 颜色
turtle.color('red', 'pink')
# 笔粗细
turtle.pensize(3)
# 速度
turtle.speed(100)
# 提笔
turtle.up()
# 隐藏笔
turtle.hideturtle()
# 去到的坐标,窗口中心为0,0
turtle.goto(0, -200)
turtle.showturtle()
# 画上线
turtle.down()
turtle.speed(100)
turtle.begin_fill()
turtle.left(140)
turtle.forward(200)
# 调用画爱心左边的顶部
LittleHeart()
#  调用画爱右边的顶部
turtle.left(120)
LittleHeart()
# 画下线
turtle.speed(100)
turtle.forward(200)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.showturtle()
#第一句话
turtle.speed(1)
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('LightSalmon', 'pink')
turtle.write("刚好遇见你", font=('algerian', 30,), align="center")
turtle.up()
turtle.showturtle()

window = turtle.Screen()
window.exitonclick()
#turtle.done()
