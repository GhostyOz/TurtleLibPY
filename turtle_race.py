from turtle import Turtle,Screen
import random
name = ''
def race():
    global name
    finish_line_passed = False
    while not finish_line_passed:
        for i in turtles:
            i.forward(random.randint(1,20))
            if i.xcor() >= 250:
                name = i.pencolor()
                finish_line_passed = True
                break
            else:
                finish_line_passed = False
    return name

def result(bet,winner):
    if bet == winner:
        print('Your choice won!!')
    else:
        print(f'Your choice lost, the winner is {winner}')

racer = int(input("Enter the number of racers (Max 9): "))
colors = ['red','green','blue','magenta','cyan','yellow','salmon','pink','orange','lawngreen']
turtles = []
screen = Screen()
screen.setup(600,600)
screen.title("Turtle Racing")
ypos = -50
for racers in range(1,racer +1):
    tim = Turtle('turtle')
    tim.color(colors[racers])
    tim.penup()
    tim.setposition(-250,ypos)
    ypos += 30
    turtles.append(tim)

user_bet = screen.textinput('Bets here!','Place your bet(Write the color : ').lower()
wins = race()
result(user_bet,wins)
screen.exitonclick()



