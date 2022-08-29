import turtle
import pandas
from turtle import Screen
FONT = ('Arial', 6, 'bold')
TOTAL_STATES = 50
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.bgpic(image)
turtle.hideturtle()
turtle.penup()
score = 0
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < len(states):
    user_input = screen.textinput(title=f"{score}/{TOTAL_STATES}", prompt="What's the state name").title()

    if user_input in states:
        guessed_states.append(user_input)
        position = data[data.state == user_input]
        x = int(position.x)
        y = int(position.y)
        turtle.goto(x, y)
        turtle.write(f"{user_input}", move=False, align='center', font=FONT)
        score += 1

    if user_input == "Exit":

        missed_states = [state for state in states if state not in guessed_states]
        data_dict = {
            "missed_states": missed_states
        }
        data1 = pandas.DataFrame(data_dict)
        data1.to_csv("states_to_learn.csv")

        break
