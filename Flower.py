import turtle
colors=['purple','blue','green','red','yellow','white']
t=turtle.Pen()
turtle.bgcolor('black')
for i in range(100):
    t.speed(200)
    t.pencolor(colors[i%6])
    t.forward(150)
    t.left(59)
turtle.done()