def fc(food,color):
    for food, color in zip(food, color):
        print(food,"color is", color)
a = ["Apple", "Banana", "Carrot"]
b = ["Red", "Yellow", "Orange"]
fc(a,b)

