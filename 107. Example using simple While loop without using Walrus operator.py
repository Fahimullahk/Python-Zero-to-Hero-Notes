foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
    break
  foods.append(food)
print(foods)


"""In the above example we created an empty list and used a while loop. 
Inside the loop we created a variable and passed it a user input to write 
the names of food he likes. After that we used the if statement with the 
condition that if the user writes the quit then the program will breaks/ends, 
and the last we append the user input food in the foods list. However we can 
write the same program in the below form by using the Walrus operators."""
