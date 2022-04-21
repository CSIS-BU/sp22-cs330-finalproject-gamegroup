import random
from colorama import init, Back, Fore
import sys 
import socket 
init()

wordList = ["Pilot", "Pound", "Queen", "Ratio", "Shock", "Sheep", "Skill"]
word = random.choice(wordList).lower()

BUFFER_SIZE = 2048 
 
def main():
    
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python3 wordle.py [Server IP] [Server Port]") 
    server_ip = sys.argv[1] 
    server_port = int(sys.argv[2]) 
    client(server_ip, server_port) 
    
    """TODO: Open socket and send message from sys.stdin""" 
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    
        # now connect to server 
        s.connect((server_ip, server_port)) 
    
        word = s.recv(BUFFER_SIZE) 
        if not data: break
            
        #This is for testing purposes, just prints out the chosen word.
        print("The server chose: " + word)

        # Inform player of general rules
        print("You've been randomly assigned a 5 letter word. \n"
              "You have 5 attempts to guess the correct word.")

        # The player has 5 attempts to guess
        for attempts in range(1, 5):
            print("Guess #" + str(attempts) + ": ")

            guess = sys.stdin.buffer.read(BUFFER_SIZE) 

            sent = s.sendall(guess) 
             
            if sent == 0: 
                raise RuntimeError("socket connection broken")
           
            data = clientsocket.recv(BUFFER_SIZE) 
            if not data: break
           
            response = ""
            for i in range(len(data)):
                #Compare each letter of the guessed word to the correct word and change it's color, print response to the player.
                if guess[i] == "1":
                    #Green and yellow wasn't really working in my terminal so I'm using these for now
                    response += Back.CYAN + Fore.BLACK + word[i] + Fore.RESET + Back.RESET
                elif guess[i] == "2":
                    response += Back.YELLOW + Fore.BLACK + word[i] + Fore.RESET + Back.RESET
                else:
                    response += word[i] + Back.RESET
            print(response)

            
            
            flag = s.recv(BUFFER_SIZE) 
            
            #If the user guesses the word correctly then the game is over
            if flag == "YES":
                print("You guess correctly!!")
                break;

if __name__ == "__main__":
    main()
