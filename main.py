import random

from os import system, name
from hangman_wordslist import word_set
from hangman_art import stages, logo

def clear():
  
# for windows
    if name == 'nt':
        _ = system('cls')
# for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

random_word = random.choice(word_set)
length = len(random_word)
life = 6
end = False
print(logo)


ans = []
for _ in range(length):
    ans += "_"
print(" ".join(ans))
print()

while not end:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in ans:
        print(f"You have already guessed {guess}")

    for l in range(length):
        letter = random_word[l]
        if letter == guess:
            ans[l] = letter

    if guess not in random_word:
        print(f"Oops {guess} is not in the word. You lose a life !")
        life -= 1

        if life == 0:
            end = True
            print("You lose!")
    
    print(" ".join(ans))

    if "_" not in ans:
        end = True
        print("Yay, You win!")

    print(stages[life])