import random
import pycountry
import string
import tkinter as tk

# Define global variables for chance_label and letters_label
global chance_label, letters_label

def choose_country():
    countries = [country.name.replace(" ", "").upper() for country in pycountry.countries if len(country.name) < 15]
    country = random.choice(countries)
    possible_letters = set(country)
    extra_letters = random.choices(string.ascii_uppercase, k=5)  # Select 5 random letters
    possible_letters.update(extra_letters)
    return country, possible_letters

def display_word(hidden_word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in hidden_word)

def process_guess(hidden_word, guessed_letters, guess):
    if guess in guessed_letters:
        return False
    guessed_letters.add(guess) 
    return guess in hidden_word

def draw_hangman(canvas, step):
    body_parts = {
        1: (20, 200, 100, 200),    # Base
        2: (60, 200, 60, 50),      # Stand
        3: (60, 50, 155, 50),      # Top Stand
        4: (155, 50, 155, 80),     # Rope
        5: (125, 80, 185, 130),    # Head (oval)
        6: (155, 130, 155, 170),   # Body 
        7: (155, 130, 125, 150),   # Left Arm
        8: (155, 130, 180, 150),   # Right Arm
        9: (155, 170, 125, 200),   # Left Leg
        10: (155, 170, 185, 200)   # Right Leg
    }
    for i in range(1, step + 1):
        if i == 5:
            canvas.create_oval(*body_parts[i], width=2)
        else:
            canvas.create_line(*body_parts[i], width=2)

def stop_game():
    global chances
    chances = 0
    draw_hangman(canvas, 10)  # Display full hangman

def restart_game():
    global hidden_word, guessed_letters, chances, chance_label, letters_label
    stop_game()
    canvas.delete("all")
    
    # Recreate game elements in the current window
    hidden_word, possible_letters = choose_country()
    guessed_letters = set()
    chances = len(hidden_word) + 2
    
    output_var.set(display_word(hidden_word, guessed_letters))
    chance_label.config(text="Chances left: {}".format(chances))
    letters_label.config(text="Possible letters: " + ' '.join(possible_letters))
    draw_hangman(canvas, 0)  # Reinitialize Hangman drawing

def on_guess():
    global chances
    if chances == 0:
        output_var.set("Game over! Please restart to play again.")
        return
    guess = entry.get().upper()
    entry.delete(0, tk.END)
    if len(guess) != 1 or not guess.isalpha():
        output_var.set("Please enter a single letter!")
        return
    if process_guess(hidden_word, guessed_letters, guess):
        if display_word(hidden_word, guessed_letters).replace(" ", "") == hidden_word:
            output_var.set("Congratulations! You guessed the country: " + hidden_word)
            stop_game()
        else:
            output_var.set(display_word(hidden_word, guessed_letters))
    else:
        chances -= 1
        chance_label.config(text="Chances left: {}".format(chances))
        output_var.set("Incorrect guess. Chances left: " + str(chances))
        output_var.set(display_word(hidden_word, guessed_letters))
        draw_hangman(canvas, len(hidden_word) + 2 - chances)
        if chances == 0:
            output_var.set("You ran out of chances. The country was: " + hidden_word)
            stop_game()

def start_game():
    global hidden_word, guessed_letters, chances, chance_label, letters_label
    hidden_word, possible_letters = choose_country()
    guessed_letters = set()
    chances = len(hidden_word) + 2
    
    window = tk.Tk()
    window.title("Country Hangman Game")

    tk.Label(window, text="Welcome to Country Hangman!").pack()
    chance_label = tk.Label(window, text="You have {} chances to guess the country.".format(chances))
    chance_label.pack()
    letters_label = tk.Label(window, text="Possible letters: " + ' '.join(possible_letters))
    letters_label.pack()

    global output_var
    output_var = tk.StringVar()
    output_var.set(display_word(hidden_word, guessed_letters))
    tk.Label(window, textvariable=output_var).pack()

    global entry
    entry = tk.Entry(window)
    entry.pack()

    tk.Button(window, text="Guess", command=on_guess).pack()
    tk.Button(window, text="Restart", command=restart_game).pack()

    global canvas
    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()
    draw_hangman(canvas, 0)  # Initialize Hangman drawing

    window.mainloop()

if __name__ == "__main__":
    start_game()
