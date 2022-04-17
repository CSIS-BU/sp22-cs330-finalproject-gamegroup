import random
from colorama import init, Back, Fore
init()

wordList = ["Pilot", "Pound", "Queen", "Ratio", "Shock", "Sheep", "Skill"]
word = random.choice(wordList).lower()

def main():
    #This is for testing purposes, just prints out the chosen word.
    print("The server chose: " + word)

    # Inform player of general rules
    print("You've been randomly assigned a 5 letter word. \n"
          "You have 5 attempts to guess the correct word.")

    # The player has 5 attempts to guess
    for attempts in range(1, 5):
        print("Guess #" + str(attempts) + ": ")

        guess = input()

        response = ""
        for i in range(len(word)):
            #Compare each letter of the guessed word to the correct word and change it's color, print response to the player.
            if guess[i] == word[i]:
                #Green and yellow wasn't really working in my terminal so I'm using these for now
                response += Back.CYAN + Fore.BLACK + guess[i] + Fore.RESET + Back.RESET
            elif guess[i] in word:
                response += Back.YELLOW + Fore.BLACK + guess[i] + Fore.RESET + Back.RESET
            else:
                response += guess[i] + Back.RESET
        print(response)

        #If the user guesses the word correctly then the game is over
        if word == guess:
            print("You guess correctly!!")
            break;

if __name__ == "__main__":
    main()
