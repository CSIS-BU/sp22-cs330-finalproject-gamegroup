# CS 330: Final Project


## Requirements:
	1. Valid installation of python
	2. Colorama, Install using "pip install colorama"
	
## How to start:
	* Start the server using "python server.py [Port_Number]" 
	* Start the client using "python client.py 127.0.0.1 [Server_Port_Number]"

## How the game works:
	Guess a five letter word within 6 tried
	
	If you guess a letter correctly and in the correct spot, the letter turns cyan
	
	If you guess a letter correctly and in the wrong spot, the letter turns yellow
	
	If you guess a letter incorrectly, the letters do not change color
	
	The server can handle multiple client connections, so only one instance of server.py is necessary.
	Upon connection the server generates a random 5 letter word for each client connection, it is not consistent between clients.