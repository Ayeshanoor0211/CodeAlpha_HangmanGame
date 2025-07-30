# Hangman Game

Welcome to the Hangman Game — a fun and interactive text-based game built with Python!  
This project is part of the **CodeAlpha Python Programming Internship**.

##  Overview

The player has to guess a randomly chosen word, one letter at a time.  
With only **6 wrong guesses allowed**, it's a race to figure out the word before the game ends!

## 🔧 Features

-  5 predefined words
-  Random word selection
-  Loops and conditionals to control game flow
-  Console-based user interaction
-  Clear win/loss outcome
-  Beginner-friendly Python code

## 🧠 Concepts Used

- `random` module
- `while` loop
- `if-else` conditions
- `input()` / `print()` for I/O
- `lists`, `strings`, and `sets`

## 📌 Sample Output
Welcome to Hangman!
Guess the word: _ _ _ _ _ _
Enter a letter: a
❌Wrong guess. Attempts left: 5
Word: _ _ _ _ _ _
Enter a letter: p
✅Correct guess!
Word: p _ _ _ _ _
Enter a letter: y
✅Correct guess!
Word: p y _ _ _ _
Enter a letter: t
✅Correct guess!
Word: p y t _ _ _
Enter a letter: l
❌Wrong guess. Attempts left: 4
Word: p y t _ _ _
Enter a letter: o
✅Correct guess!
Word: p y t _ o _
Enter a letter: n
✅Correct guess!
Word: p y t _ o n
Enter a letter: h
✅Correct guess!
Word: p y t h o n
🎉Congratulations! You guessed the word: python
