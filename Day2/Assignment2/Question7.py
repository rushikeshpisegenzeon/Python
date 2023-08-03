
Countries = ["Finland","Germany","Sweden","Ireland","Turkey"]

result = filter(lambda country: "and" in country,Countries)
print(list(result))