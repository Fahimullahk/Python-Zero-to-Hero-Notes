print("======== Encoding ========")
word = input("Enter your secret word...")
word1 = list(word)
word3 = word1[0]
word1.pop(0)
word1.append(word3)
word4 = input("Enter any three random words....")
word5 = list(word4)
if ((len(word5)) == 3):
    word1.extend(word5)
    word5.extend(word1)
    for i in word5:
        print(i, end="")
else:
    word1.reverse()
    for i in word1:
        print(i, end="")

