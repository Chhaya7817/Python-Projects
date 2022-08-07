import turtle
a=10
colors=['purple','blue','green','red','yellow','white']
pen=turtle.Pen()
for i in range(a*4):
    pen.pencolor(colors[i%6])
    pen.forward(i*10)
    pen.right(90)
turtle.done()