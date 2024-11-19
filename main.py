from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"  # Background color for the app interface
current_card = {}  # This will store the current word to be displayed

# Try loading previously learned words, else load the default list of words
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # The file storing words the user still needs to learn
except FileNotFoundError:
    original = pandas.read_csv("data/french_words.csv")  # Default CSV of French words and their English translation
    to_learn = original.to_dict(orient="records")  # Convert the CSV into a list of dictionaries
else:
    to_learn = data.to_dict(orient="records")  # If the file exists, load the words to learn

# Function to show the next word
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)  # Cancel any previous flip timer
    current_card = random.choice(to_learn)  # Select a random word from the list
    canvas.itemconfig(c_title, text="French", fill="black")  # Set title to French
    canvas.itemconfig(c_word, text=current_card["French"], fill="black")  # Show the French word
    canvas.itemconfig(card_background, image=card_front)  # Set the front card image
    flip_timer = window.after(3000, func=flip_card)  # Set a timer to flip the card after 3 seconds

# Function to flip the card to show the English translation
def flip_card():
    global current_card
    canvas.itemconfig(c_title, text="English", fill="white")  # Set title to English
    canvas.itemconfig(c_word, text=current_card["English"], fill="white")  # Show the English translation
    canvas.itemconfig(card_background, image=card_back)  # Change the card image to the back side

# Function to handle when the user marks the word as "known"
def is_known():
    to_learn.remove(current_card)  # Remove the known word from the list
    data_new = pandas.DataFrame(to_learn)  # Convert the updated list back to a DataFrame
    data_new.to_csv("data/words_to_learn.csv", index=False)  # Save the updated list to the CSV
    next_card()  # Show the next card

# Function to handle when the user marks the word as "not known"
def not_known():
    next_card()  # Show the next card

# Window setup
window = Tk()
window.title("Flash-Cards-French(100)")  # Set window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set window padding and background color

flip_timer = window.after(3000, func=flip_card)  # Start the flip timer

# Canvas setup for the flashcard design
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")  # Load the front card image
card_back = PhotoImage(file="images/card_back.png")  # Load the back card image
card_background = canvas.create_image(400, 263, image=card_front)  # Set the card's background
c_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))  # Set title as French
c_word = canvas.create_text(400, 263, text=f"word", font=("Ariel", 60, "bold"))  # Display the word in large font
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Set the canvas background color and remove borders
canvas.grid(row=0, column=0, columnspan=2)  # Add the canvas to the window layout

# Button images for correct and incorrect responses
rb_img = PhotoImage(file="images/wrong.png")  # Image for the "wrong" button (red)
red_button = Button(image=rb_img, highlightthickness=0, command=not_known)  # Button to mark the word as unknown
red_button.grid(row=1, column=0)

gb_img = PhotoImage(file="images/right.png")  # Image for the "right" button (green)
green_button = Button(image=gb_img, highlightthickness=0, command=is_known)  # Button to mark the word as known
green_button.grid(row=1, column=1)

# Start the flashcard app with the first card
next_card()

# Keep the app running
window.mainloop()
