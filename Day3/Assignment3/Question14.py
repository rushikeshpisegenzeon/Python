
Countries = ["Finland","Germany","Sweden","Ireland","Turkey"]

result = list(filter(lambda country: "and" in country,Countries))

print(result)