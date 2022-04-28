#!/usr/bin/python
import sys
import socket
import random
from _thread import *

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

# Open the file as read
wordFile = open("wordList.txt", "r")
wordList = []

# Clean up the file contents
for eachLine in wordFile:
    wordList.append(eachLine.replace("\n", ""))

def client_handler(clientsocket):

    # Choose a random word
    wordOfTheDay = random.choice(wordList).lower()

    # Debugging, print out the word of the day.
    print(wordOfTheDay)

    with clientsocket:
        while True:
            # receive data and print it out
            guess = clientsocket.recv(RECV_BUFFER_SIZE)
            guess = guess.decode()
            result = ""

            # creates a string of numbers that represents whether the letter is in the correct place
            # is contained within the word of the day or doesn't exist at all
            print(guess)

            # Capitalize the first letter to match the word list
            guess = guess.lower()

            for i in range(len(guess)):
                # print(result) #DEBUG
                # print(guess[i]) #DEBUG
                # print(wordOfTheDay[i]) #DEBUG
                if guess[i] == wordOfTheDay[i]:
                    result += '0'
                elif guess[i] in wordOfTheDay:
                    result += '1'
                else:
                    result += '2'

            print(result + '\n')

            clientsocket.send(result.encode())

            if not guess:
                break

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        # bind the socket to the host and its port 
        serversocket.bind(('', server_port))
        # prepare for connection 
        serversocket.listen(QUEUE_LENGTH)

        while True:
            # accept connections from outside 
            (clientsocket, address) = serversocket.accept()

            start_new_thread(client_handler, (clientsocket, ))
    pass


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()
