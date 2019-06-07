import socket
import threading
import hashlib
import sys

bind_ip = "127.0.0.1"
bind_port = 5175

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))

#client-handling thread

known_teams = {}

def verify_seed(incoming):
    seed = hashlib.sha256(incoming[2]).hexdigest()
    if seed[-1 * int(incoming[0]):] == "0"*int(incoming[0]):
        return 1

def handle_client(client_socket):

    incoming = client_socket.recv(1024)
    incoming = incoming.split("-")
    print("[*] Hash set recieved: %s" % incoming)
    #send back a packet

    if (verify_seed(incoming)):
        print("[*] Seed Verified ")
    else:
        print("[*] Seed Verification Failed, Rejecting")
        exit(0)

    score = (16**int(incoming[0]))/2
    if incoming[1] in known_teams:
        known_teams[incoming[1]] += score
    else:
        print("[*] New team discovered: " + incoming[1])
        known_teams[incoming[1]] = score

    print("[*] Score of " + incoming[1] + " now " + str(known_teams[incoming[1]]))

    client_socket.send("200")
    client_socket.close()

while True:

    client,addr = server.accept()
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
