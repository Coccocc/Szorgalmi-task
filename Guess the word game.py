# Author: Hegyi Dáneil 
# Neptune code: CJC6AN
# Email: rekellemail5@gmail.com
# Created: 2023-11-02
# Last Modified: 2023-11-03





import random

words_to_guess = [
    "kutya",
    "macska",
    "alma",
    "ház",
    "autó",
    "iskola",
    "társaság",
    "kávé",
    "televízió",
    "cím",
    "nyelv",
    "számítógép",
    "szép",
    "barát",
    "egészség",
    "élet",
    "víz",
    "zene",
    "virág",
    "színes",
    "kert",
    "ablak",
    "állat",
    "tudomány",
    "konyha",
    "város",
    "szabadidő",
    "híd",
    "munka",
    "egyedül"
]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word_to_guess = choose_random_word(words_to_guess)
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print("You need to guess a word with {} letters.".format(len(word_to_guess)))

    while True:
        print("\nCurrent word: " + display_word(word_to_guess, guessed_letters))
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Yey! You guessed the word: " + word_to_guess)
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

        guess = input("Guess a letter or type 'quit' to end the game: ").lower()

        if guess == "quit":
            break
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter or 'quit'.")
        elif guess in guessed_letters:
            print("You've already guessed this letter. Please choose another one.")
        else:
            guessed_letters.append(guess)

if __name__ == "__main__":
    main()
