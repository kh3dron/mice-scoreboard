#Mice: a holistic scorekeeping mechanism for networked wargames

**Introduction**

MICE, (Miner-Imitating Counter Executables) a new scoring mechanism for network wargames. This system uses proof-of-work miner-like programs (Mice) to evaluate network control over time, for use in networking or security simulations.

This repository holds both the Server and the Client for the MICE scoreboard. The client file should be given to students/players, and the server should be run on its own.

**About MICE**

I developed the MICE system for my position as a summer research assistant for Dr. Jens Mache with Lewis & Clark ROGERS Program. I was really fascinated by the idea of proof-of-work hash solving, and wanted to incorperate it into a way of improving CTF exercises, which I feel can be too easy to cheat in sometimes. Hence, Mice.

**Installation and Usage**

The two programs, mouse.py and server.py, refer to the player program and the scoreboard, respectively. The Scoreboard should be started and run at the beginning of the game and kept running throughout the exercise.

**For Players**:

If you are a player, download the mouse.py file. The mouse should be run like this:

`python mouse.py <owner> <scoreboard IP> <port`

When you run your mice, use your team name as the owner parameter. If the owner isn't right, the mouse will generate points for someone else. The exact rules for where, when, and how to use your mice are a matter of your simulation administrator.

**For Scorekeepers / Administrators:**

Every simulation needs at least one scoreboard server running to collect points. Download the server.py program, and run it like this:

`python server.py <ip> <port>`

The server will then listen for clients to broadcast to it, in the form of solved hash sets. The server will then keep score for all players, and give readouts of realtime network statistics. In the majority of exercises, you'll want to tell your players the IP and port of the scoreboard, unless finding the scoreboard is itself a part of your exercise.

**Upcoming** **Features**

-Clients abale to send to Multiple servers

-Better endgame reporting

-More details in the readme
