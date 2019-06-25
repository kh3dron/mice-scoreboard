import socket
import threading
import hashlib
import sys

def usage():
    print("""
    [+] Mouse Scorekeeper SERVER- run to keep score. Usage:
    [+] python server.py <ip:port>
    """)

if len(sys.argv) != 2:
    usage()
    exit(0)

#globals
terms = sys.argv[1].split(":")
bind_ip =           terms[0]
bind_port =         int(terms[1])
total_score =       0.0
known_teams =       {}
server =            socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def metric_hashrate(count):
    count = str(count)
    if len(count) < 4:
        return count + " H"
    elif len(count) < 7:
        return count[:-3] + " KH"
    elif len(count) < 10:
        return count[:-6] + " MH"
    elif len(count) < 13:
        return count[:-9] + " GH"
    elif len(count) < 16:
        return count[:-12] + " TH"
    elif len(count) < 19:
        return count[:-15] + " PH"
    elif len(count) < 22:
        return count[:-18] + " EH"
        #damn son

def verify_seed(incoming):
    seed = hashlib.sha256(incoming[2]).hexdigest()
    if seed[-1 * int(incoming[0]):] == "0"*int(incoming[0]):
        return 1

def handle_client(client_socket):

    incoming = client_socket.recv(1024)
    incoming = incoming.split("-")
    #print("[*] Hash set recieved: %s" % incoming)

    if (verify_seed(incoming)):
        print("[*] Seed Verified ")
    else:
        print("[*] Seed Verification Failed, Rejecting")
        client_socket.send("Unsolved Hash")
        client_socket.close()
        exit(0)

    score = (16**int(incoming[0]))
    if incoming[1] in known_teams:
        known_teams[incoming[1]] += score
    else:
        print("[*] New team discovered: " + incoming[1])
        known_teams[incoming[1]] = score

    global total_score
    total_score += score
    dom = str(round((known_teams[incoming[1]]/total_score) * 100, 1)) + "%"

    print("[*] Score of "+incoming[1]+" now "+metric_hashrate(known_teams[incoming[1]]))
    print("    Network control of team "+incoming[1]+" now "+str(dom))
    client_socket.send("OK")
    client_socket.close()

def main():

    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] MICE Scoreboard ready on %s:%d" % (bind_ip, bind_port))

    while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

main()
