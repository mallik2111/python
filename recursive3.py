def fibonaci(x):
    n = 0
    m = 1
    y = x
    k = 1
    if x ==0:
        print(x)
    elif x==1:
        print(n,x)
    else:
        print(n)
        while k<y:
            print(m)
            z = n + m
            n = m
            m = z
            k+=1
            
            
        
    
fibonaci(10)
