def fact(n):
    if n == 1:
        return 1
    
    else:
        return n * fact(n-1)

m = fact(4)
print(m)