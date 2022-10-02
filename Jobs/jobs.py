import os

def schedule_api():
    print("EVERY 10 seconds this executed")

    for i in os.listdir("me"):
        os.remove(f"me/{i}")