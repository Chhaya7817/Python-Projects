import turtle
def draw_square(brad):
    for i in range(4):
        brad.right(90)
        brad.forward(100)
def bent_square(brad):
    brad.right(5)
        
brad=turtle.Pen()
window=turtle.Screen()

window.bgcolor('black')
brad.color("red")
brad.speed(100)
for i in range(80):
    draw_square(brad)
    bent_square(brad)


