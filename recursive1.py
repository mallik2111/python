def sum(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return sum(n-1) + sum(n-2)

print(sum(4))
