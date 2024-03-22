# Country-Hangman-Game
These are the instructions that are given below:
- Set Up Your Word List: Create a list of countries to serve as potential secret words for the game.
- Random Selection: Use the random module to select a country from the list as the secret word.
- Game Mechanics: Define a function to display the current state of the secret word, with underscores for unguessed letters and the actual letters for correct guesses.
- Guessing Chances: Allocate the number of chances for the player to guess the word. The number of chances is the length of the country name plus 2.
- Letter Guess: Write a function to process the player guess. If the guessed letter is in the word, reveal its position(s).
- Winning Condition: Define a winning condition that checks if the player has guessed all the letters in the country name.
- Losing Condition: The game ends when the player runs out of chances.
- User Interaction: Set up the main game loop that prompts the user to enter a guess and provides feedback.
For example, if the randomly selected country is "Canada," then the player would get 7 chances in total, since "Canada" has 6 letters.

---------------------------------------------------------------------------------
Let's go through the code step by step:

# Imports:
random: Used for generating random values.
pycountry: A Python library providing information about countries.
string: A Python module containing common string operations.
tkinter: The standard GUI (Graphical User Interface) library for Python.

# Global Variables:
chance_label and letters_label: These are declared as global variables because they are accessed and updated within multiple functions.

# choose_country() function:
This function selects a country randomly from a list of countries obtained using the pycountry library.
It generates a set of possible letters from the chosen country, along with 5 additional random letters.

# display_word() function:
It displays the hidden word (the country name) with underscores for letters that have not been guessed yet.

# process_guess() function:
This function processes the user's guess.
If the guess has already been made, it returns False.
Otherwise, it adds the guess to the set of guessed letters and returns True if the guess is in the hidden word.

# draw_hangman() function:
This function draws the hangman figure based on the number of incorrect guesses (step).
It uses a dictionary (body_parts) to define coordinates for each part of the hangman figure.

# stop_game() function:
This function stops the game by setting the global variable chances to 0 and drawing the full hangman.

# restart_game() function:
This function resets the game state by stopping the game, clearing the canvas, choosing a new hidden word,
resetting guessed letters, and resetting the number of chances.

# on_guess() function:

This function is called when the user makes a guess.
It checks if the game is still ongoing and processes the guess accordingly.
If the guess is incorrect, it decreases the chances, updates the UI, and draws the next part of the hangman.
If the guess is correct and the entire word has been guessed, it displays a congratulatory message.
If the user runs out of chances, it displays a message indicating the end of the game.

# start_game() function:

This function initiates the game by setting up the GUI window using Tkinter.
It initializes the UI elements such as labels, buttons, entry field, and canvas for drawing.
It sets up event handlers for button clicks.

-------------------------------------------------------------------------------------------------------

Finally, it starts the Tkinter event loop to handle user interactions.
The code essentially creates a simple hangman game where the player needs to guess a country's name. The player has a limited number of chances to guess the correct letters, and a hangman figure is drawn progressively for each incorrect guess.


      
