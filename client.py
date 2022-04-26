import sys
import socket

SEND_BUFFER_SIZE = 2048
RECV_BUFFER_SIZE = 2048

# Zech and Ethan both wrote and figured out the logic of code

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # now connect to server 
        s.connect((server_ip, server_port))

        while guessCount < 6:
            # content = sys.stdin.buffer.read(SEND_BUFFER_SIZE)

            # Take the user's input as a guess
            guess = ""
            guessCount = 0
            while (len(guess) < 5 or len(guess) > 5):
                guess = input()
                guessCount += 1

                if (len(guess) < 5 or len(guess) > 5):
                    print("Guess must be five letters.")

            guess = guess.lower()

            # Encode and send that guess to the server
            sent = s.sendall(guess.encode())

            # Accept code from the server
            guessCode = s.recv(RECV_BUFFER_SIZE)

            response = ""

            # Decode the code from server to the response for player
            for i in range(len(guessCode)):
                # Compare each letter of the guessed word to the correct word and change it's color, print response to the player.
                if guessCode[i] == "1":
                    #Green and yellow wasn't really working in my terminal so I'm using these for now
                    response += Back.CYAN + Fore.BLACK + word[i] + Fore.RESET + Back.RESET
                elif guessCode[i] == "2":
                    response += Back.YELLOW + Fore.BLACK + word[i] + Fore.RESET + Back.RESET
                else:
                    response += word[i] + Back.RESET

            # Print out the response in color according to right/wrong letters
            print(response.decode())

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
