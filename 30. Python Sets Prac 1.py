cities = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities2 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities3 = {"Tokyo", "Berlin", "Kabul", "Multan"}
cities4 = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities5 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities6 = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities7 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
union1 = cities.union(cities2)
cities.update(cities2)
Intersect1 = cities2.intersection(cities3)
cities2.intersection_update(cities3)
symdif = cities4.symmetric_difference(cities5)
cities4.symmetric_difference_update(cities5)
dif = cities6.difference(cities7)
cities6.difference_update(cities7)
print("The union of cities and cities2 is :", union1)
print("When we write cities.update(cities2) the update method applied on cities set i.e:", cities)
print("The intersection between cities2 and cities3 is :", Intersect1)
print("The intersection_update changes the cities2 items when we write cities2.intersection_update(cities3)", cities2)
print("The symetric_difference of cities4 and cities5 is :", symdif)
print("When we write cities4.symmetric_difference_update(cities5) is changes cities4 :", cities4)
print("The difference method between cities6 and cities7 is :", dif)
print("The difference_update method applied on cities6 when we write cities6.difference_update(cities7):", cities6)

