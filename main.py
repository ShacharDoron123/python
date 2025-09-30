
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True



def choose_word(file_path, index):
    file = open(file_path, "r")
    content = file.read()
    file.close()
    words = content.split()
    word_index = (index - 1) % len(words)
    chosen_word = words[word_index]
    return chosen_word


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
        0: """     
     +---+
     |   |
         |
         |
         |
         |
    =========
""",
        1: """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
        2: """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
        3: """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ===========""",
        4: """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
        5: """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
        6: """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
"""
    }
    print(HANGMAN_PHOTOS.get(num_of_tries))


def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        print("old_letters : \t" + ' -> '.join(sorted(old_letters_guessed)))
        return True
    else:
        print("X")
        print("You entered an old guess/more than 2 letters/not an english letter\n old_letters : \t" + ' -> '.join(sorted(old_letters_guessed)))
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def main():
    HANGMAN_ASCII_ART = r""" 
                _    _  
               | |  | |  
               | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
               |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
               | |  | | (_| | | | | (_| | | | | | | (_| | | | |
               |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |                      
                                   |___/                       
    """

    MAX_TRIES = 6
    print("Welcome to the game Hangman\n" + HANGMAN_ASCII_ART + "\n" + "Number of wrong guesses :\t" + str(MAX_TRIES))

    file_path = input("Please enter the path to the word file: ")
    index = int(input("Please enter the index of the word to guess: "))

    secret_word = choose_word(file_path, index)
    secret_word = secret_word.lower()

    print("\n" * 30)

    old_letters_guessed = []
    num_of_tries = 0

    print_hangman(num_of_tries)
    print("\n")
    print(show_hidden_word(secret_word, old_letters_guessed))
    print("\n")

    while num_of_tries <= MAX_TRIES:
        if check_win(secret_word, old_letters_guessed):
            print("congrats you won!!! (: \n The word was: " + secret_word)
            break

        if num_of_tries == MAX_TRIES:
            print("\n" * 30)
            print_hangman(num_of_tries)
            print("nice try but you lost ): \n The word was: " + secret_word)
            break

        guess = input("Enter the first letter : ")
        guess = guess.lower()
        valid_guess = try_update_letter_guessed(guess, old_letters_guessed)

        while not valid_guess:
            guess = input("Enter a letter: ").lower()
            valid_guess = try_update_letter_guessed(guess, old_letters_guessed)

        print("\n" * 30)

        if valid_guess:
            if guess not in secret_word:
                print(":(")
                num_of_tries += 1

        print("\n")
        print_hangman(num_of_tries)
        print("\n")
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("\n")


if __name__ == "__main__":
    main()
