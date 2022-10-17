from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

password_list = password_letters + password_symbols + password_numbers
shuffle(password_list)
password = "".join(password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate():
    password_entry.insert(0,password)
    pyperclip.copy(password)


def delete():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or password == "":
        messagebox.showerror(title="Error", message="Empty slots")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            data_file = open("data_file.txt", "a")
            data_file.write(f"{website} | {email} | {password}\n")
            data_file.close()
            delete()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


canvas = Canvas(height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0,)

website_label = Label(text="Website:" )
website_label.grid(column=0, row=1,)

website_entry = Entry(width=48)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=10, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
