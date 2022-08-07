import turtle


def draw_dream():
    window=turtle.Screen()
    window.bgcolor('white')
    draw_scarlett()
    window.exitonclick()
    


def draw_scarlett():
    brad=turtle.Turtle()
   # brad.speed(200)
    brad.shape("turtle")
    brad.color("purple")
    draw_head(brad)
    draw_body(brad)
    draw_arm(brad)
    draw_leg1(brad)
    draw_leg2(brad)
    draw_face(brad)
    


def draw_head(brad):
    brad.color("cyan")
    brad.begin_fill()
    brad.circle(60)
    brad.end_fill()
    brad.speed(3)
    brad.right(60)

def draw_body(brad):
    brad.color("blue")
    num=0
    brad.begin_fill()
    while num<3:
         brad.forward(150)
         brad.right(120)
         brad.speed(1)
         num+=1
    brad.end_fill()

def draw_arm(brad):
    brad.forward(60)
    brad.left(60)
    brad.forward(80)

    brad.backward(80)
    brad.right(60)
    brad.backward(60)

    brad.right(60)

    brad.forward(60)
    brad.right(60)
    brad.forward(80)

    brad.backward(80)
    brad.left(60)
    brad.forward(90)


def draw_leg1(brad):
    brad.left(120)
    brad.forward(40)
    brad.right(90)
    brad.forward(120)
    draw_foot1(brad)
    

def draw_leg2(brad):
   brad.color("blue")
   brad.right(180)
   brad.forward(120)
   brad.right(90)
   brad.forward(70)
   brad.right(90)
   brad.forward(120)
   draw_foot2(brad)


def draw_foot1(brad):
   brad.color("red")
   num=0
   brad.begin_fill()
   while num <4:
       brad.forward(20)
       brad.right(90)
       num+=1
   brad.end_fill()

def draw_foot2(brad):
   brad.color("green")
   num=0
   brad.begin_fill()
   while num <4:
       brad.forward(20)
       brad.left(90)
       num+=1
   brad.end_fill()


def draw_face(brad):
    brad.color("black")
    draw_eye(brad)
    draw_nose(brad)
    draw_mouth(brad)
def draw_eye(brad):
    #eye1
    brad.up()
    brad.goto(-30,75)
    brad.down()
    brad.circle(10)
    brad.circle(3)
    brad.up()
    #eye2
    brad.goto(20,75)
    brad.down()
    brad.circle(10)
    brad.circle(3)
def draw_nose(brad):
    brad.up()
    brad.goto(0,45)
    brad.down()
    brad.color("red")
    brad.begin_fill()
    brad.circle(5)
    brad.end_fill()
def draw_mouth(brad):
    brad.up()
    brad.goto(-15,40)
    brad.down()
    brad.right(10)
    brad.circle(20,195)
    brad.up()
    brad.goto(1,17)
    brad.down()
    brad.begin_fill()
    brad.right(180)
    brad.circle(5,180)
    brad.end_fill()
    brad.hideturtle()

    
draw_dream()