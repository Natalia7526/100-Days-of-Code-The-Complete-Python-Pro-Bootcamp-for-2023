import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    round_up_cans = math.ceil(number_of_cans)
    return print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input("Put the hight of wall (m)\n"))  # Height of wall (m)
test_w = int(input("Put the width of wall (m)\n"))  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
