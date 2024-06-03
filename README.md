# Ping-Pong Game

This is ping-pong game implemented using FastAPI and a CLI tool. The game consists of two servers that ping each other at regular intervals, and it can be controlled commands like pause, resume, and stop from the CLI tool with also spicify the internal time.

## Features

- Start, pause, resume, and stop the game
- Set the interval between pings

# Example commands to use
python pong-cli.py start 8000 2000 ("2000" is time intervel)

python pong-cli.py pause 8000 

python pong-cli.py resume 8000 

python pong-cli.py stop 8000 


## Installation

### Step 1: Clone the Repository
   ```bash
   git clone https://github.com/AASHIK-coder/ping-pong-game
   cd ping-pong-game

### Step 2: Set Up a Virtual Environment

Set up a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi uvicorn requests
```

## Project Structure

The main scripts for the server and CLI tool are located in the `Scripts` folder:

- `server.py`: The FastAPI server that handles ping-pong interactions.
- `pong-cli.py`: The CLI tool to control the game (start, pause, resume, stop).

## Usage

### Step 1: Start the Server Instances

You need to start two instances of the server on different ports. Open two terminal windows and run the following commands:

- Terminal 1:
  ```bash
  uvicorn Scripts.server:app --port 8000
  ```

- Terminal 2:
  ```bash
  uvicorn Scripts.server:app --port 8001
  ```

### Step 2: Use the CLI Tool to Control the Game

Open a third terminal window to use the CLI tool to control the game. Navigate to the `Scripts` directory:

```bash
cd Scripts
```

Use the following commands to control the game:

- **Start the Game**:
  ```bash
  python pong-cli.py start 8000 1000
  ```
  This command starts the game on the server running on port 8000 with a 1000 milliseconds interval between pings.

- **Pause the Game**:
  ```bash
  python pong-cli.py pause 8000
  ```
  This pauses the game on the server running on port 8000.

- **Resume the Game**:
  ```bash
  python pong-cli.py resume 8000
  ```
  This resumes the game on the server running on port 8000.

- **Stop the Game**:
  ```bash
  python pong-cli.py stop 8000
  ```
  This stops the game on the server running on port 8000.
