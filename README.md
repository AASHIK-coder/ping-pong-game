# Ping-Pong Game

This is ping-pong game implemented using FastAPI and a CLI tool. The game consists of two servers that ping each other at regular intervals, and it can be controlled commands like pause, resume, and stop from the CLI tool with also spicify the internal time.

# Example commands to use
python pong-cli.py start 8000 2000 ("2000" is time intervel)
python pong-cli.py pause 8000 
python pong-cli.py resume 8000 
python pong-cli.py stop 8000 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR_GITHUB_USERNAME>/ping-pong-game.git
   cd ping-pong-game
