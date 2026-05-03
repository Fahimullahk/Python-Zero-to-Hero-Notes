Stdname = input("Write the name of a person")
Substudied = input("Which subject he Studied")
qulifyexam = int(input("Write the qualification"))
Marksobt = int(input("Write the Persentage"))
if (qulifyexam < 14):
     print(Stdname, "may be eligible for the job but needs to focus on the skill")
elif (qulifyexam == 14):
    print(Stdname, "qualified the Bechelor program in the field of" , Substudied)
    if (Marksobt >= 70):
          print ("He is eligible for the job")
    elif (Marksobt >= 80):
          print("He is perfect for the job")
    elif (Marksobt > 60 & Marksobt < 70):
         print ("He may get the job but he needs to work hard for getting experience")
elif (qulifyexam == 16):
    print(Stdname, "qualified the Bechelor program in the field of" , Substudied)
    if (Marksobt >= 70):
          print ("He is eligible for the job")
    elif (Marksobt >= 80):
          print("He is perfect for the job")
    elif (Marksobt > 70):
         print ("He may get the job but he needs to work hard for getting experience")
elif (qulifyexam > 16):
     print(Stdname, "qualified M-Phil or PHD in the field of", Substudied)
     print("He need not to apply for any job, whereas the job itself coming towards", Stdname)
else:
     print("I just practicing Python programming.......")

