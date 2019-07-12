import hashlib
import sys
import socket
import time
import random

def usage():
    print("""
    [+] Mouse Scorekeeper CLIENT- point to scoreboard, and run to gain points. Usage:
    [+] python mouse.py <owner> <ip:port>
    [+] Add more <ip:port> pairs seperated by comma to send to multiple scoreboards.
    [+] Examples:
    [+] python mouse.py thomas 10.10.10:7000
    [+] pythom mouse.py khedron 10.10.10.10:9000,10.10.11:9005
    """)
if len(sys.argv) < 3:
    usage()
    exit(0)

"""
PLAYERS - You may be allowed to tamper with this program if your instructor permits.
Modify with caution, especialy functions which modify submission formatting (solve())
and submission handling (send_solve()). Submissions either not sent or sent with
improper formatating will not count towards your score. 
"""

#globals
difficulty =        5
owner =             sys.argv[1]
ips =   []
ports = []
server_count = 0

for g in (sys.argv[2].split(",")):
    server_count += 1
    set = g.split(":")
    ips.append(str(set[0]))
    ports.append(int(set[1]))

def solve(owner, difficulty):
    nonce = 0
    seed = owner + str(time.time())
    while(1):
        attempt = seed + str(nonce)
        tried = hashlib.sha256(attempt).hexdigest()
        if tried[-difficulty:] == "0"*difficulty:
            final = str(difficulty) + "-" + owner + "-" + attempt
            return final
        else:
            nonce +=1

def send_solve(seed, ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
    except:
        print("[*] Failed to connect to MICE Server at "+ip+":"+str(port)+", exiting")
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
    global ips

    while(1):
        made = solve(owner, difficulty)
        for g in (range(server_count)):
            send_solve(made, ips[g], ports[g])

main()
