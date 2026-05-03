countries = ("Turkey", "Pakistan", "India", "England", "Germany")
abc = list(countries)
abc.append("Australlia")
abc.pop(3)
abc[2] = "Afghanistan"
countries = tuple(abc)
print(countries)

