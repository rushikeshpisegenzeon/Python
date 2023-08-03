statelist = ["Delhi","Bihar","UP","Goa","Gujarat","Assam","AP"]
result = ''
for state in statelist:
    ch = state[-2]
    ch.lower()
    print(ch)
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' :
        result+=ch

n_res = result.upper()[::-1]
print("final output: ",n_res)