## **Mice: a holistic scorekeeping mechanism for networked wargames**

#Introduction

MICE, (Miner-Imitating Counter Executables) a new scoring mechanism for network wargames. This system uses proof-of-work miner-like programs (Mice) to evaluate network control over time, for use in networking or security simulations.

This repository holds both the Server and the Client for the MICE scoreboard. The client file should be given to students/players, and the server should be run on its own.

I developed the MICE system for my position as a summer research assistant for Dr. Jens Mache with Lewis & Clark ROGERS Program. I was really fascinated by the idea of proof-of-work hash solving, and wanted to incorperate it into a way of improving CTF exercises, which I feel can be too easy to cheat in sometimes. Hence, Mice.

#Installation and Usage

The two programs, mouse.py and server.py, refer to the player program and the scoreboard, respectively. The Scoreboard should be started and run at the beginning of the game and kept running throughout the exercise.

**For Players**:

If you are a player, download the mouse.py file. The mouse should be run like this:

`python mouse.py <owner> <scoreboard IP:port>`

To send to multiple scoreboards, append more IP:port combinations with a comma, like this:

`python mouse.py <owner> 10.10.10.1:7000,10.10.10.2:8000`

When you run your mice, use your team name as the owner parameter. If the owner isn't right, the mouse will generate points for someone else; owner names are case sensetive. The exact rules for where, when, and how to use your mice are a matter of your simulation administrator. In most games, you'll want to be able to copy your mice to run more of them, so keep your original download somewhere safe. 

*Note:* If a mouse fails to connect to any one of its listed scoreboards, it will quit. This should be kept in mind when giving a mouse many scoreboards, as it could be more succeptible to instability. 

**For Scorekeepers / Administrators:**

Every simulation needs at least one scoreboard server running to collect points. Download the server.py program, and run it like this:

`python server.py <ip> <port>`

The server will then listen for clients to broadcast to it, in the form of solved hash sets. The server will then keep score for all players, and give readouts of realtime network statistics. In the majority of exercises, you'll want to tell your players the IP and port of the scoreboard, unless finding the scoreboard is itself a part of your exercise. You'll also most likely want to tell players not to tamper with or attack the scoreboard- it should be left out of scope for the game, unless, again, that's intentionaly not the case. 

#Game design ideas

The Mice system is highly adaptable for lots of different kinds of games. Here's some of the simpler examples to consider when designing a use case for the Mice scoreboard:

**Blue team v. Red team:** All mice should be run with the owner "Red", and only allowed to be run on blue team workstations. The blue team should aim to keep the red team score as low as possible by hardening their workstations from attack and eliminating any mice they find. The red team should try to keep as many mice alive on the blue network as they can. 

**Network mapping / Enumeration:** Students are each given their own mice. Administrators should set up the scoreboards hidden on their network, and leave it up to students to find them and connect to as many as they can. 

**BATTLE ROYALE:** Jen's favorite game mode. Every student has their own team and a workstation; they are then responsible for propogating their mice through other workstations to run more copies of themselves. 



**Upcoming** **Features**

-Better endgame reporting

-Hash uniqueness checking / no double submissions

-More details in the readme
