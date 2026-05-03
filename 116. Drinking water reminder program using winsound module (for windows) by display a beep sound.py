import time
import winsound

def set_reminder(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    winsound.Beep(1000, 1000)
    print("Assalamualaikum Fahim Ullah, It time for drinking a glass of water")

set_reminder(60)

