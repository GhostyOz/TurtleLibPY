from turtle import Turtle,Screen
import random
# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab02/colors Possible colors
def square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)

def dashed_line():
    for i in range(10):
        timmy.pendown()
        timmy.forward(15)
        timmy.penup()
        timmy.forward(15)

def drawing_shapes_w_random_color():
    for i in range(3,10):
        angle =(360/i)
        timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for j in range(i):
            timmy.forward(100)
            timmy.right(angle)

def random_walk(iterations,distance):
    for i in range(iterations):
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        directions = [0,90,180,270]
        direction = random.choice(directions)
        timmy.setheading(direction)
        timmy.forward(distance)

def draw_circles():
    r = 100
    j = 0
    for i in range(1,36):
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.setheading(j)
        timmy.circle(r)
        j +=10 # gapsize !! buna göre range ayarla

colormode = 255
timmy = Turtle()
timmy.color('blue1')
timmy.shape('turtle')
timmy.speed(200)
#timmy.pensize(5)

myScreen = Screen()
myScreen.colormode(colormode)
# square()
#dashed_line()
#drawing_shapes_w_random_color()
#random_walk(50,40)
draw_circles()


myScreen.canvheight = 500
myScreen.canvwidth = 500
myScreen.exitonclick()






