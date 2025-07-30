import random

def hangman():
    words = ["apple", "code", "python", "intern", "alpha"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌Wrong guess. Attempts left: {attempts}")

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("🎉Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The correct word was:", word)

hangman()
