def cum():
    b = ""
    c = ""
    a = "Odds and Ends"
    for i in range(len(a)):
        if i%2 == 0:
            b += a[i]
        else:
            c+= a[i]
        if i ==6:
            return (b + c)
        
result = cum()
print(result)
