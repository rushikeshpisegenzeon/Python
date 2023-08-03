
statelist = ["Delhi","Bihar","Goa","Gujarat","Assam"]
result = ''
for state in statelist:
    inde_=state.__len__()//2
    ch = state[inde_]
    #print(ch)
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
        result+=ch
print(result.upper())
