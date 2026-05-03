questions = [
    ["During which month do Muslims observe fasting?", "A) Muharram", "B) Ramadan", "C) Shawwal", "D) Dhul-Hijjah", "B"], 
    ["Who was known as 'The Sword of Allah'?", "A) Abu Bakr", "B) Umar", "C) Khalid bin Waleed", "D) Ali", "C"], 
    ["Name of the cave for the first revelation?", "A) Thawr", "B) Hira", "C) Uhud", "D) Kahf", "B"], 
    ["How many Surahs are in the Quran?", "A) 110", "B) 112", "C) 114", "D) 120", "C"], 
    ["Who was the first Prophet in Islam?", "A) Ibrahim", "B) Muhammad", "C) Adam", "D) Musa", "C"], 
    ["Which city is the 'Land of Prophets'?", "A) Makkah", "B) Madinah", "C) Palestine", "D) Cairo", "C"]
]
ilevels = [1000, 2000, 3000, 5000, 10000, 20000]
level = 0
for i in range(len(questions)):
    print("\nYour question No", i + 1, "is:")
    print(questions[i][0])
    print(questions[i][1], "  ", questions[i][2])
    print(questions[i][3], "  ", questions[i][4])
    
    reply = input("Enter your choice (A, B, C, or D): ").strip().upper()

    if reply == questions[i][5]:
        # level = ilevels[i]
        print("Correct! Your Intelligence level is:", ilevels[i])
    else:
        print("Incorrect answer!")
        print("The correct answer was:", questions[i][5])
        break

