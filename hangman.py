from random import choice
print("H A N G M A N")
wins = 0
lost = 0
def game(letter):
    words_tup = ('python', 'java', 'swift', 'javascript')
    secret_word = choice(words_tup)
    hint = ['-' for x in range(len(secret_word))]
    list_of_letters = []
    list_of_mistakes = []
    counter = 8
    while counter > 0:
        if "-" not in hint:
            print("You guessed the word " + secret_word + "!")
            global wins
            wins += 1
            print("You survived!")
            break
        print(f"\n{''.join(hint)}")
        guess = input("Input a letter: ")
        if guess in list_of_letters or guess in list_of_mistakes:
            print("You've already guessed this letter.")
        elif len(guess) != 1:
            print("Please, input a single letter.")
        elif guess.isupper() == True or guess.isalpha() == False or guess.isdigit():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif guess in secret_word:
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    hint[i] = guess
                    list_of_letters.append(guess)
        else:
            print("That letter doesn't appear in the word.")
            list_of_mistakes.append(guess)
            counter -= 1
        if "-" in hint and counter == 0:
            print("You lost!")
            global lost
            lost += 1

guess = "a"

while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    enter = input()
    if enter == "play":
        game(guess)
    elif enter == "results":
        print("You won: " + str(wins) + " times.")
        print("You lost: " + str(lost) + " times.")
    else:
        break
