from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time
import threading

app = FastAPI()

class PongTime(BaseModel):
    pong_time: int

port = 8000
target_port = 8001
target_url = f"http://127.0.0.1:{target_port}/ping"
pong_time_ms = 1000
game_thread = None
pause_event = threading.Event()
stop_event = threading.Event()

@app.post("/ping")
async def ping():
    """Respond to ping with 'pong'."""
    return "pong"

@app.post("/set_pong_time")
async def set_pong_time(pong_time: PongTime):
    """Endpoint to update the pong time."""
    global pong_time_ms
    pong_time_ms = pong_time.pong_time
    return {"message": "Pong time updated", "pong_time_ms": pong_time_ms}

def send_ping():
    """Send a ping after waiting for pong_time_ms."""
    while not stop_event.is_set():
        pause_event.wait()  #waiting,if the event is cleared (paused)
        time.sleep(pong_time_ms / 1000)
        try:
            response = requests.post(target_url)
            if response.status_code == 200:
                print("Ping sent and pong received!")
            else:
                print("Failed to receive pong.")
        except requests.RequestException:
            print("Failed to send ping.")
        if stop_event.is_set():
            break

@app.post("/start")
async def start_game():
    """Start the game."""
    global game_thread
    if game_thread is None or not game_thread.is_alive():
        stop_event.clear()
        pause_event.set()
        game_thread = threading.Thread(target=send_ping)
        game_thread.start()
    return {"message": "Game started"}

@app.post("/pause")
async def pause_game():
    """Pause the game."""
    pause_event.clear()
    return {"message": "Game paused"}

@app.post("/resume")
async def resume_game():
    """Resume the game."""
    pause_event.set()
    return {"message": "Game resumed"}

@app.post("/stop")
async def stop_game():
    """Stop the game."""
    stop_event.set()
    return {"message": "Game stopped"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=port)
