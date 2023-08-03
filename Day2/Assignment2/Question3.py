
statelist = ["Delhi","Telengana","Goa","AP","Kerala"]
result=''
for state in statelist:
     result += ''.join([state[0].lower() + state[-1].upper()])
print(result)




