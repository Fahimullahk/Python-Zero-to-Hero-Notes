cities = {"Tokyo", "Istanbul", "Berlin", "Peshawar"}
cities2 = {"Tokyo", "Islamabad", "Rawalpindi", "Karachi"}
cities3 = {"Multan", "Lahore", "Karachi", "Faisalabad"}
cities4 = {"Tokyo", "Istanbul", "Peshawar"}
cities5 = {"Charsadda", "Wah", "Sawabi"}
cities6 = {"Charsadda", "Wah", "Sawabi"}
cities7 = {"Charsadda", "Wah", "Sawabi"}
isdisjoint1 = cities.isdisjoint(cities2)
isdisjoint2 = cities.isdisjoint(cities3)
issuperset1 = cities.issuperset(cities2)
issuperset2 = cities.issuperset(cities4)
issubset1 = cities4.issubset(cities)
cities4.add("Kabul")
cities5.update(cities)
cities3.remove("Multan")
popi = cities6.pop()
cities7.clear()
print("When we apply isdisjoint method and write cities.isdisjoint(cities2) :", isdisjoint1)
print("When we apply isdisjoint method and write cities.isdisjoint(cities3) :", isdisjoint2)
print("when we apply issuperset method and write cities.issuperset(cities2): ", issuperset1)
print("When we apply issuperset method and write cities.issuperset(cities4): ",issuperset2)
print("When we apply issubset method and write cities4.issubset(cities) :",issubset1)
print("When we add Kabul in cities4 with add method :", cities4)
print("When we apply update method and write cities5.update(cities): ", cities5)
print("""When we apply remove method and write cities3.remove("Multan") : """, cities3)
print("When we apply pop method on cities6 it removes the last item : ", popi)
print("when we apply clear method on cities7 it wil clear all the set and return an empty set : ", cities7)

