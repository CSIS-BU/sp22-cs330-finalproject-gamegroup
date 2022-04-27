#!/usr/bin/python\
from colorama import Fore, Back, Style
import sys
import socket

SEND_BUFFER_SIZE = 2048
RECV_BUFFER_SIZE = 2048

# Zech and Ethan both wrote and figured out the logic of code

def instructions():
    # Instructions
    print("Welcome to Wordle! Your objective is to guess the correct word.\n")

    print("If your guess looks like this: ", end='')
    print(Back.CYAN + Fore.BLACK + 'x' + Fore.RESET + Back.RESET, end='')
    print(" it's the right letter in the right place!")

    print("If your guess looks like this: ", end='')
    print(Back.YELLOW + Fore.BLACK + 'x' + Fore.RESET + Back.RESET, end='')
    print(" it's the right letter in the wrong place!")

    print("And if your guess looks like this: ", end='')
    print('x' + Back.RESET, end='')
    print(" that letter is wrong entirely!\n")

    print("You have a total of six guesses to get the word. Good luck!\n")


def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # now connect to server 
        s.connect((server_ip, server_port))

        instructions()

        guessCount = 0

        while guessCount < 6:
            # content = sys.stdin.buffer.read(SEND_BUFFER_SIZE)

            # Take the user's input as a guess
            # print("TEST") DEBUG
            guess = "word"

            while (len(guess) != 5):
                # print("26") DEBUG

                print(guessCount + 1, end = '')
                print("/6")
                guess = input("Enter your guess: ")

                if (len(guess) != 5):
                    print(Fore.RED + "Guess must be five letters.")
                    print(Style.RESET_ALL)

            # print(guess) #DEBUG

            guessCount += 1

            guess = guess.lower()

            # Encode and send that guess to the server
            sent = s.sendall(guess.encode())

            # Accept code from the server
            guessCode = s.recv(RECV_BUFFER_SIZE)

            guessCode = guessCode.decode()

            #print(guessCode) #DEBUG

            # Decode the code from server to the response for player
            # Print out the response in color according to right/wrong letters
            for i in range(len(guessCode)):
                # Compare each letter of the guessed word to the correct word and change it's color, print response to the player.

                #Correct place and letter
                if guessCode[i] == "0":
                    #Green and yellow wasn't really working in my terminal so I'm using these for now
                    print(Back.CYAN + Fore.BLACK + guess[i] + Fore.RESET + Back.RESET, end = '')
                #Correct letter, wrong place
                elif guessCode[i] == "1":
                    print(Back.YELLOW + Fore.BLACK + guess[i] + Fore.RESET + Back.RESET, end = '')
                #Incorrect letter incorrect place
                else:
                    print(guess[i] + Back.RESET, end = '')

            print('\n')

            # If it doesn't send error out
            if sent == 0:
                raise RuntimeError("socket connection broken")


            if guessCode == "00000":
                print("You won! Congrats :)")
                break
            elif guessCount == 6:
                print("You lost! Better luck next time :(")

        pass


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)


if __name__ == "__main__":
    main()
