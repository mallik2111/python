def main():
   num = int(input("Enter a integer: "))
   print("The factorial of num is", fact(num))


def fact(n):
    if n==0:
        return 1
    else:
        y=n-1    
        while(y!=0):
            n=n*y
            y-=1
        return n


main()
