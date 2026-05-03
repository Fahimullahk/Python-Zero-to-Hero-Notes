print("======== Decoding ========")
word = input("Enter your Encoded words...")
word_ = input("Enter your three Random encoded words...")
wordn = list(word_)
word1 = list(word)
if (len(wordn) == 3):
    del word1[0:3]
    del word1[-3: ]
    word2 = list(word1[-1])
    word1.pop(-1)
    word2.extend(word1)
    for i in word2:
        print(i, end="")
else:
    word1.reverse()
    word3 = list(word1[-1])
    word1.pop(-1)
    word3.extend(word1)
    for i in word3: 
       print(i, end="")

