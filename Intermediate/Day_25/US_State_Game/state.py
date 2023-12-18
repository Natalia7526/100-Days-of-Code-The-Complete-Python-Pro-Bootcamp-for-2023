from turtle import Turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

class State(Turtle):
    def __init__(self):
        super(State, self).__init__()
        self.penup()
        self.hideturtle()

    def add_name(self):
        data.loc[data["state"] == self.
        data.loc[data["state"] == answer_state]["y"]
        new_x = int(selected_data_X.iloc[0])
        new_y = int(selected_data_Y.iloc[0])
        self.goto(new_x, new_y)
        self.write(str(answer_state), False, align="center")




