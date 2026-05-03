f = open("myfile.txt", "r")       # Here it will read the file i created
i = 0 # Here i starting the indexing of my file element with will denote the student name
while True: # Here i am starting a while loop, so it will continue when the subsequence condition remains true.
    i = i+1 # Here i am starting the index number from 1 by adding i with 1.
    line = f.readline() # Here i using readline() method which will be applied on my created file
    if not line: # Here if no more element exists means here a condition says that the line will continue till the last element in line.
        break # Here if no more element found, then it will breaks the while from further execution.
    m1 = line.split(",")[0] # Here its splits very first element which is on 0 index seperated by "," from each line and apply it to every subject.
    m2 = line.split(",")[1] # Here its splits second element which is on 1 index seperated by "," from each line and apply it to every subject.
    m3 = line.split(",")[2] # Here its splits third element which is on 2 index seperated by "," from each line and apply it to every subject.
    print(f"The marks of student {i} in English is : {m1}") # Now here we used the "f" string print the students with marks
    print(f"The marks of student {i} in Math is : {m2}")
    print(f"The marks of student {i} in Physics is : {m3}")

