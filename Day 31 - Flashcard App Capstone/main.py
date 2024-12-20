from tkinter import *
from pandas import *
import threading
import random

BACKGROUND_COLOR = "#B1DDC6"
french_word = ""
english_word = ""
to_learn = {}

# Read the CSV into a data frame using pandas and convert data frame to a list of dictionaries
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_random_word():
    """Generates a new random word to display on the flash card."""
    #Disables the use of buttons while showing word
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")
    # Declare variables as global
    global french_word
    global english_word
    global to_learn
    global current_card
    # Find random word pair
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        print("No More Words")
        exit()
    french_word = current_card['French']
    english_word = current_card['English']
    # Clears the associated tagged text
    canvas.delete("word_text")
    canvas.delete("title")
    # Configures canvas image to front of card with new title and word
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"), tag="word_text")
    canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), tag="title")
    # Uses threading module to initiate the flip card function after 4 seconds
    threading.Timer(4, flip_card).start()


def flip_card():
    """After specified amount of time in new_random_word function, flip card revealing translation"""
    # Enables the use of buttons
    wrong_button.config(state="normal")
    right_button.config(state="normal")
    # Clears the associated tagged text
    canvas.delete("word_text")
    canvas.delete("title")
    # Configures canvas image to back of card with english title and word
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.create_text(400, 263, text=english_word, font=("Ariel", 60, "bold"), tag="word_text", fill="white")
    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), tag="title", fill="white")


def save_progress():
    """Removes words from list that have been displayed and saves words to learn in a new csv"""
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy the Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# The canvas object allows me to layer things on top of eachother
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# For future reference, don't try and create a photoimage in a function
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- Buttons ------------------------------- #
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, borderwidth=0, command=new_random_word)
wrong_button.grid(row=1, column=0)

# The lambda lets me call two functions at the same time when pressing the button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=lambda: [new_random_word(), save_progress()])
right_button.grid(row=1, column=1)

canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), tag="title")
canvas.create_text(400, 263, text=new_random_word(), font=("Ariel", 60, "bold"))

window.mainloop()
