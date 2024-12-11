from tkinter import *
from tkinter import messagebox
# Need to import messagebox because it's not a class
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a password by randomly selecting letters,numbers, and symbols. Popup will be updated when button is
    pressed and password will be copied onto the clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for n in range(randint(8, 10))]
    symbols_list = [choice(symbols) for n in range(randint(2, 4))]
    numbers_list = [choice(numbers) for n in range(randint(2, 4))]
    # These lists are using python list comprehension

    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)
    # Adds lists together and shuffles all of the characters

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)
#     Joins the characters in the password list and copies to clipboard using pyperclip


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """If fields are unpopulated an error popup will occur. Otherwise, information is saved to a data.json file and
     fields are cleared."""

    website = website_field.get()
    username = username_field.get()
    password = password_field.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        #     Utilizes messagebox from tkinter to create a popup
        messagebox.showerror(title="Error", message="Please do not leave any fields empty!")
    else:
        try:
            # Reading old data and checking exception if file is empty
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        except json.decoder.JSONDecodeError:
            data = {}
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data
            data.update(new_data)

            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)

        finally:
            website_field.delete(0, 'end')
            password_field.delete(0, 'end')


# ---------------------------- Search ------------------------------- #
def find_password():
    """Searches JSON file to retrieve login information for user specified website. If website has no information or
    no data file, a popup will appear to convey that to the user."""

    try:
        website = website_field.get()
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website} Login Info",
                                message=f"Username: {username}\nPassword: {password}", )
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website: ")
website.grid(row=1, column=0)

username = Label(text="Email/Username: ")
username.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)

# Entry Fields
website_field = Entry(width=35)
website_field.focus()
website_field.grid(row=1, column=1, columnspan=2, sticky='ew')

username_field = Entry(width=35)
username_field.grid(row=2, column=1, columnspan=2, sticky='ew')
username_field.insert(0, "hunter@email.com")
# Can change this field to common username/email so it does not need to be entered each time

password_field = Entry(width=21)
password_field.grid(row=3, column=1, sticky='ew')

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky='ew')

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky='ew')

window.mainloop()

