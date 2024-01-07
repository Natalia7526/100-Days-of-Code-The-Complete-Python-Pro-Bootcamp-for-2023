import random
from tkinter import *
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------ #
GREEN = "#b1ddc6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=GREEN)

# The flash card
canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
# position is half of height and width of canvas -> if image have to be in the center
canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)


# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=generate_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

window.mainloop()
