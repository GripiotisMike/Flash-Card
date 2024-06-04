from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/french_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(c_title, text="French", fill="black")
    canvas.itemconfig(c_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(c_title, text="English", fill="white")
    canvas.itemconfig(c_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data_new = pandas.DataFrame(to_learn)
    data_new.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def not_known():
    next_card()


window = Tk()
window.title("Flash-Cards-French(100)")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
c_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
c_word = canvas.create_text(400, 263, text=f"word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

rb_img = PhotoImage(file="images/wrong.png")
red_button = Button(image=rb_img, highlightthickness=0, command=not_known)
red_button.grid(row=1, column=0)

gb_img = PhotoImage(file="images/right.png")
green_button = Button(image=gb_img, highlightthickness=0, command=is_known)
green_button.grid(row=1, column=1)

next_card()

window.mainloop()
