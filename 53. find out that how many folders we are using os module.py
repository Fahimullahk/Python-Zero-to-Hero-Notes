import os
Folders = os.listdir("Pract")
for Folder in Folders:
    print(Folder)
    print(os.listdir(f"data/{Folder}"))

