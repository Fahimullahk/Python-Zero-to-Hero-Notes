import os
os.makedirs(r"D:\folderi", exist_ok=True)
# fst_path = "D:\folderi\abc"
for i in range(0, 100):
    with open(fr"D:\folderi\abc{i+1}.png", "w") as f:
        f.write("Hello this file is in folderi!!")

