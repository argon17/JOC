import random
from replit import clear
from hangman_arts import logo, stages
from words import words_list


chosen_word = random.choice(words_list)
word_length = len(chosen_word)

#print(f'Pssst, the chosen word is {chosen_word}')
print(logo)

display = list('_'*word_length)
print(' '.join(display))
print('\n')

gameEnded = False
lives = 7

while not gameEnded:

    guess = input('Guess a letter: ').lower()
    clear()
    if guess in display:
        print(f"You have already guessed the letter '{guess}'")

    for position in range(word_length):
        if chosen_word[position]==guess:
            display[position] = guess

    if guess not in chosen_word:
        lives-=1
        print(f"Letter '{guess}' is not present in the word.")

        if lives==0:
            gameEnded = True
            print('You lost.')
            print(f'The letter was {chosen_word}.')

    print(' '.join(display))

    if not "_" in display:
        gameEnded = True
        print('You win')

    
    print(stages[6-lives])

