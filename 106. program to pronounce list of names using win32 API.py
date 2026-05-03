import win32com.client as wincl
l = ["Abdul Salam", "Fahim Ullah", "Mudassir", "Haris Jan", "Muhammad Yousaf", "Muhammad Aliyaar Fahim"]
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) 
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) 
for item in l:
    spk.Speak(f"Salam to, {item}")

