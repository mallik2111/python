def function(n):
    if n <= 1:
        return 1
    else:
        return function(n-1) + function(n-2)


print (function(80))