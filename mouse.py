import hashlib
import sys
import socket
import time
import random

def usage():
    print("""
    [+] Mouse Scorekeeper CLIENT- run to gain points. Usage:
    [+] python mouse.py <owner> <scoreboard IP> <port>
    """)
if len(sys.argv)!= 4:
    usage()
    exit(0)

#globals
difficulty =        5
owner =             sys.argv[1]
ip =                sys.argv[2]
port =          int(sys.argv[3])

def solve(owner, difficulty):
    nonce = 0
    seed = owner + str(time.time())
    while(1):
        attempt = seed + str(nonce)
        tried = hashlib.sha256(attempt).hexdigest()
        if tried[-difficulty:] == "0"*difficulty:
            final = str(difficulty) + "-" + owner + "-" + attempt
            return final
            break
        else:
            nonce +=1

def send_solve(seed):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
    except:
        print("[*] Failed to connect to MICE Server, exiting")
        exit(0)

    client.send(seed)
    response = (client.recv(4096))
    if (response == "OK"):
        print("[*] Solution submitted at difficulty " + str(difficulty))
    else:
        print("[*] Submission error: " + str(response))

#Main

def main():

    global difficulty
    global owner
    global ip

    while(1):
        made = solve(owner, difficulty)
        send_solve(made)

main()
