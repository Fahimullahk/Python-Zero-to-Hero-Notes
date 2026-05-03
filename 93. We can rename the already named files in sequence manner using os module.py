import os
for i in range(0, 100):
    if os.path.exists(fr"D:\folderi\abc{i+1}.png"):
        os.rename(fr"D:\folderi\abc{i+1}.png", fr"D:\folderi\{i+1}.png")

