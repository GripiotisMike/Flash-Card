# Flash Card - French Vocabulary Learning App

A simple flashcard application built using Python's `Tkinter` and `pandas` that helps users learn French vocabulary. The app displays French words and their English translations, allowing the user to mark them as "known" or "not known". Words that are marked as known are saved for later review.

---

## Features

- **Flashcards**: Randomly shows French words and their English translations.
- **Timed Flip**: The French word is displayed first, and after a 3-second delay, the English translation is shown.
- **Mark Words**: The user can mark words as "known" or "not known" with simple button clicks.
- **Progress Tracking**: Words marked as "known" are removed from the learning list and saved in a CSV file for future study.
- **Data Persistence**: If the user has already learned some words, their progress is saved and reloaded automatically.

---

# Setup

### Prerequisites

1. **Python**: This project requires Python 3.x.
2. **Required Libraries**: Install the required Python libraries by running:

   ```bash
   pip install pandas
3. Ensure you have the following files in the correct structure:
- french_words.csv (in data/): This file contains the French-English vocabulary pairs.
- words_to_learn.csv (in data/): This file tracks the words that the user still needs to learn (it will be automatically created and updated).
- Images for the flashcards and buttons in the images/ folder.

# How to Run

1. Clone the repository or download the project files to your local machine.
2. Open a terminal or command prompt and navigate to the directory where main.py is located.
3. Run the app using the command: python main.py
4. The application window will open, showing French flashcards. Use the Right (green) and Wrong (red) buttons to mark the words as known or not known. Progress is automatically saved.

# Functionality
1. Start: When the app is opened, a French word is displayed.
2. Flip: After 3 seconds, the English translation is shown on the back of the card.
3. Mark Known: If the user knows the word, they click the Right button, and the word is removed from the study list.
4. Mark Not Known: If the user does not know the word, they click the Wrong button, and the word will be presented again later.
5. Progress Saving: All known words are saved in words_to_learn.csv so they won't be shown again in future sessions.
