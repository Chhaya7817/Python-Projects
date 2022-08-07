import turtle
import random
def draw_moon(brad):
    brad.right(90)
    brad.begin_fill()
    brad.circle(150,380)
    brad.end_fill()
    
    brad.begin_fill()
    brad.color('black')
    brad.circle(120,360)
    brad.end_fill()
    brad.color('white')
    
def draw_star(brad):
    for i in range(5):
        brad.forward(10)
        brad.right(144)
def change_pos(brad):
    brad.end_fill()
    brad.up()
    brad.goto(random.randint(-800,800),random.randint(-800,800))
    brad.begin_fill()
    brad.down()

brad=turtle.Pen()
window=turtle.Screen()
posX=-200
posY=-150
brad.goto(posX,posY)
window.bgcolor('black')
brad.speed(200)
brad.color('white')
draw_moon(brad)
change_pos(brad)
for i in range(100):
    draw_star(brad)
    change_pos(brad)
brad.onclick()