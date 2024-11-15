import random

# Word list for the game
WORD_LIST = ["Shahzaib", "Developer", "Internship", "python", "Cognorise", "javascript", "hangman", "programming", "Infotech", "software"]

# Hangman display states
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Select a random word
def select_random_word():
    return random.choice(WORD_LIST)

# Game logic
def play_hangman():
    word = select_random_word().upper()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMAN_STAGES) - 1

    # Display initial empty figure and underscores for the word
    print("Welcome to Hangman!")
    print(HANGMAN_STAGES[0])
    display_word = ["_"] * len(word)
    print(" ".join(display_word))

    # Game loop
    while incorrect_guesses < max_attempts and "_" in display_word:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        # Display current hangman state and word state
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: ", " ".join(display_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

    # Win or loss check
    if "_" not in display_word:
        print("Congratulations, you won! The word was:", word)
    else:
        print("Sorry, you lost! The word was:", word)

    # Play again prompt
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_hangman()
    else:
        print("Thank you for playing!")

# Start the game
play_hangman()
