from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    current_heading = tim.heading()
    tim.setheading(current_heading - 180)
    move_forward()
def turn_left():
    current_heading = tim.heading()
    tim.setheading(current_heading - 10)
    move_forward()
def turn_right():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    move_forward()
def clear_screen():
    tim.setposition(0, 0)
    tim.clear()
    tim.setheading(0)



screen.listen()
screen.onkey(move_forward,'w') #Event Listener (Takes function and key as input, key pressed --> function)
screen.onkey(move_backward,'s')
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')
screen.onkey(clear_screen,'c')
screen.exitonclick()