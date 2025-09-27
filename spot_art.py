from turtle import Turtle, Screen
import random
import colorgram
colors = colorgram.extract('dots.jpg',12*7)
print(colors)
rgbs = []
for color in colors:
    values = []
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    values.append((r,g,b))
    rgbs.append(values)
# Removing the background shades
rgbs.remove(rgbs[0])
rgbs.remove(rgbs[0])
rgbs.remove(rgbs[1])
rgbs.remove(rgbs[1])

def random_color_chooser():
    return random.choice(rgbs)

def random_color_circle():
    current_color = random_color_chooser()
    Ozzy.color(current_color)
    Ozzy.begin_fill()
    Ozzy.dot(20)
    Ozzy.end_fill()
    
def million_dollar_art():
    Ozzy.penup()
    Ozzy.setposition(-150,-150)
    for height in range(-120,150,30):
        for width in range(9):
            random_color_circle()
            Ozzy.penup()
            Ozzy.forward(50)
        random_color_circle()
        Ozzy.setposition(-150,height)
    Ozzy.hideturtle()

screen = Screen()
screen.setup(400,400)
screen.colormode(255)
Ozzy = Turtle()
Ozzy.shape('turtle')
Ozzy.speed(300)
million_dollar_art()
screen.exitonclick()



