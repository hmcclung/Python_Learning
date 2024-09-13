import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# This is for getting the x,y coordinates of all of the states
# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Reads a csv file of all 50 states and compiles them into a list. Keeps track of correct_answers
data = pandas.read_csv("50_states.csv")
state_list = data["state"]
new_list = state_list.to_list()
correct_answers =["STATES"]
round_one = True
score = 0

# If all 50 states have not been guessed continue loop.
# Prompts user to guess state. If correct, places name of state on map and increments how many states have been guessed
# If incorrect, refreshes prompt
# If user is done guessing and 'Exit' is typed. Ends game
while len(correct_answers) <= 50:
    correct = 0
    if round_one:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
        round_one = False
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    for state in state_list:
        if state == answer_state:
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()

            state_loc = data[data.state == answer_state]
            state_turtle.setposition(state_loc.x.item(),state_loc.y.item())
            state_turtle.write(state)

            for answers in correct_answers:
                if answers == state:
                    correct += 1
            if correct == 0:
                correct_answers.append(state)
                new_list.remove(state)
                correct = 0
                score += 1

# If user does not guess all 50 states, writes a new file of states to learn
if len(correct_answers) <= 50:
    print(new_list)
    data_dict = {
        "States": new_list
    }
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("states_to_learn")
