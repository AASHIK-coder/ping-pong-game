import sys
import requests

def send_command(command, port):
    """Send commands to the server to control the game."""
    url = f"http://localhost:{port}/{command}"
    response = requests.post(url)
    print(response.json())

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pong-cli.py <command> <port>")
    else:
        command = sys.argv[1]
        port = sys.argv[2]
        send_command(command, port)
