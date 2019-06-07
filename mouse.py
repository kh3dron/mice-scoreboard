import hashlib
import sys
import socket
import time

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

def usage():
    print("[+] Mouse Scorekeeper CLIENT- run to gain points. Usage:")
    print("[+] " + sys.argv[0] + " <user/team name>")

def send_solve(seed):
    target_host = "127.0.0.1"   #Will figure out with the server bit, later
    target_port = 5175
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    #send data
    client.send(seed)
    #receive the data
    response = client.recv(4096)
    if (response == 200):
        print("submitted seed" + seed)

#Main
if (len(sys.argv) != 2):
    usage()
    exit(0)

difficulty = 5
owner = sys.argv[1]

while(1):
    made = solve(owner, difficulty)
    print("[*] solution submitted at difficulty " + str(difficulty))
    send_solve(made)
