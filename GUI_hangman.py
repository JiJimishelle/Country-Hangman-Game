import random
import pycountry
import string
import tkinter as tk

# Define global variables for multiple functions access
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
    # Check if the game is already over
    if chances == 0:
        output_var.set("Game over! Please restart to play again.")
        return
    # Get the guessed letter from the entry widget and clear the entry
    guess = entry.get().upper()
    entry.delete(0, tk.END)
    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        output_var.set("Please enter a single letter!")
        return
    # Process the guess
    if process_guess(hidden_word, guessed_letters, guess):
        # Check if the player has guessed the entire word
        if display_word(hidden_word, guessed_letters).replace(" ", "") == hidden_word:
            output_var.set("Congratulations! You guessed the country: " + hidden_word)
            stop_game()  # End the game
        else:
            output_var.set(display_word(hidden_word, guessed_letters))  # Update displayed word
    else:
        # Decrement the chances if the guess is incorrect
        chances -= 1
        chance_label.config(text="Chances left: {}".format(chances))  # Update chances label
        output_var.set("Incorrect guess. Chances left: " + str(chances))  # Display remaining chances
        output_var.set(display_word(hidden_word, guessed_letters))  # Update displayed word
        draw_hangman(canvas, len(hidden_word) + 2 - chances)  # Update Hangman drawing

        # Check if the player has run out of chances
        if chances == 0:
            output_var.set("You ran out of chances. The country was: " + hidden_word)
            stop_game()  # End the game

def start_game():
    global hidden_word, guessed_letters, chances, chance_label, letters_label
    # Initialize game variables
    hidden_word, possible_letters = choose_country()  # Get a random country word, possible letters
    guessed_letters = set()  # store guessed letters
    chances = len(hidden_word) + 2  # Calculate the number of chances

    # Create the main game window
    window = tk.Tk()
    window.title("Country Hangman Game")
    # Display welcome message
    tk.Label(window, text="Welcome to Country Hangman!").pack()
    # Display the number of chances the player has
    chance_label = tk.Label(window, text="You have {} chances to guess the country.".format(chances))
    chance_label.pack()
    
    # Display the possible letters for the player to choose from
    letters_label = tk.Label(window, text="Possible letters: " + ' '.join(possible_letters))
    letters_label.pack()
    # Initialize a variable to display the current state of the hidden word
    global output_var
    output_var = tk.StringVar()
    output_var.set(display_word(hidden_word, guessed_letters))
    tk.Label(window, textvariable=output_var).pack()

    # Create an entry widget for the player to input their guess
    global entry
    entry = tk.Entry(window)
    entry.pack()
    # Button to submit a guess
    tk.Button(window, text="Guess", command=on_guess).pack()
    # Button to restart the game
    tk.Button(window, text="Restart", command=restart_game).pack()

    # Create a canvas for drawing the hangman
    global canvas
    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()
    draw_hangman(canvas, 0)  # Initialize Hangman drawing
    # Start the main event loop for the game window
    window.mainloop()

if __name__ == "__main__":
    start_game()
