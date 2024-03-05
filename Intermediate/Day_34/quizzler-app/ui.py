from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        # window definition
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas definition
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text="Quiz text", width=250, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        # score label definition
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, anchor="center")
        self.score_label.grid(row=0, column=1)

        # true button definition
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image)
        self.true_button.grid(row=2, column=0)

        # false button definition
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()
