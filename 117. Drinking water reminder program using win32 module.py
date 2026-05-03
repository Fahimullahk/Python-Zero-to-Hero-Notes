import time
import win32com.client

def set_reminder(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Assalamualaikum Fahim Ullah, It time for drinking a glass of water")

set_reminder(1)

