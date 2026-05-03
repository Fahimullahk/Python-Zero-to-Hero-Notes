def solutionof(name, obtmarks, Totalmarks):
    solution = (obtmarks/Totalmarks) * 100
    print(name, "got percentage =", solution,"% Marks")

a = input("Enter the name of Student")
b = int(input("Enter the total marks obtained by :"))
c = int(input("Enter the total marks"))
solutionof(a,b,c)

