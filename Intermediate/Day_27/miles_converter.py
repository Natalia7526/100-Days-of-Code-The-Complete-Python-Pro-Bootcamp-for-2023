from tkinter import *


# computing function
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


# generating layout

# generating empty window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# miles_input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# miles_label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is_equal_label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# kilometer_results_label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# kilometer_label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# calculate_button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# run the window
window.mainloop()
