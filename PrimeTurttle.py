import turtle
# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab02/colors Possible colors
ozzy = turtle.Turtle()
# ozzy.color(0.5,0.5,0.5) RGB
ozzy.color('chartreuse')
ozzy.shape('turtle')
#ozzy.shapesize(10)
ozzy.forward(100)
print(ozzy)

my_screen = turtle.Screen()
my_screen.title("My Turtle")
my_screen.exitonclick()
print(my_screen)
