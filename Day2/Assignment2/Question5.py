statelist = ["Delhi","Bihar","UP","Goa","Gujarat","Assam","AP"]
result = ''
for state in statelist:
    ch = state[1]
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
        result+=ch
n_res = result.upper()[::-1]
print(n_res)
