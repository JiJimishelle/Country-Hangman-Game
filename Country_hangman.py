import random
import pycountry

def choose_country():
    # Get a list of country names from the pycountry library
    country_names = [country.name.upper() for country in pycountry.countries]
    # Choose a random country name from the list
    return random.choice(country_names)

def display_word(hidden_word, guessed_let):
    displayed_word = ""
    for letter in hidden_word:
        # If the letter has been guessed, display it
        if letter in guessed_let:
            displayed_word += letter + ""
        # Otherwise, display an underscore
        else:
            displayed_word += "_"
    return displayed_word.strip()  # removes any leading, and trailing whitespaces

def process_guess(hidden_word, guessed_let, guess):
    if guess in guessed_let:
        # If the letter has already been guessed, inform the player
        print("You've already guessed that letter!")
        return False
    # Add the guessed letter to the set of guessed letters
    guessed_let.add(guess)
    # If the guessed letter is not in the hidden word, inform the player
    if guess not in hidden_word:
        print("Incorrect guess...")
        return False
    return True

def start_game():
    hidden_word = choose_country()
    guessed_let = set()
    # Number of chances is the length of the country name plus 2
    chances = len(hidden_word) + 2
    print("Welcome to Country Hangman Game!")
    print("You have {} chances to guess the country.".format(chances))

    while chances > 0:
        print("\nCurrent word: ", display_word(hidden_word, guessed_let))
        guess = input("Enter a letter: ").upper()

        # Validate the user input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if process_guess(hidden_word, guessed_let, guess):
            # If the player has guessed all letters in the secret word, they win
            if display_word(hidden_word, guessed_let).replace(" ", "") == hidden_word:
                print("Congratulations~ You guessed the country:", hidden_word)
                break
        else:
            # If the guess was incorrect, decrement chances
            chances -= 1
            print("Chances left: ", chances)
    else:
        # runs out of chances, they lose
        print("You ran out of chances...The country was:", hidden_word)

if __name__ == "__main__":
    start_game()
