from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# example: Amazon | angela@email.com | y26!r2KwsCn8d
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
