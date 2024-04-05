import turtle
import pandas
import time
screen = turtle.Screen()

screen.title("USA GeoGuessr")

image = "blank_states_img.gif"

screen.addshape(image)
guessed_states = []
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while len(guessed_states) < 50:
    answr_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Whats Another State's Name?").title()

    if answr_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("states_to_learn.csv")
        break

    if answr_state in all_states:
        guessed_states.append(answr_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answr_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answr_state)



screen.exitonclick()





