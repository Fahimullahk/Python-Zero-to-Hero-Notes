def fc(food,color):
    lu=[]
    for food, color in zip(food, color):
        lu.append((food,"color is", color))
    return(lu)
a = "Apple", "Banana", "Carrot"
b = "Red", "Yellow", "Orange"
print(fc(a, b))

