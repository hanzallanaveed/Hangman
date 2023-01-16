import random
import art
import words

chosen_word = random.choice(words.word_list)
print(art.logo)
print(f'Pssst, the word is {chosen_word}\n.')
lives = 6
# create an empty display which adds the "_" to the list
display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False

# while loop to end the game

while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print("You have already guessed this letter")
    # for each letter in the chosen_word, replace that specific index in display with the guessed letter if guess=chosen_word[i]
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"Guessed {guess}, you lose a life\n")

    print(f"Number of lives= {lives}\n")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(art.stages[lives])
    if lives == 0:
        end_of_game = True
        print("You Lose")

print(display)

