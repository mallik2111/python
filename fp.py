#x = float(input("what s x?"))
#y = float(input("what s y?"))
#z= round(x+y)
#print(f"{z:,}")
#print(float(input("what s x?"))+ float(input("what s y?")))
#z = x/y
#print (f"{z:.2f}")

def main():
    x= int(input("Enter a number "))
    if is_even(x):
        print("Number is even")
    else:
        print("Number is odd")

def is_even(n):
    return n%2==0

main()

def square(z):
    return pow(z,3)



def hello(to = "world"):
    print("hello", to)
    return("Hi")

main()
#name = input("what is your name? ")
hi = hello()
#print(hi)

score = int(input("Enter your score: "))
n = score%2
if n == 0:
    print(score, "Number is even")
else:
    print(score, "number is odd")
if score > 90:
    print("Grade A")
elif score > 80:
    print("Grade B")
else:
    print("Nothing")
