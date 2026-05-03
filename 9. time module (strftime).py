import time
tmst = time.strftime("%H:%M:%S")
tmst1 = int(time.strftime("%H"))
tchname = input("Write the name of teacher")
if (tmst1 >= 5) & (tmst1 < 9):
     print("Good Morning Sir :", tchname)
elif (tmst1 >= 9) & (tmst1 < 16):
     print("Good Afternoon Sir :", tchname)
elif (tmst1 >= 16) & (tmst1 < 20):
     print("Good Evening Sir:", tchname)
elif (tmst1 >= 20):
     print("Good Night Sir:", tchname)

