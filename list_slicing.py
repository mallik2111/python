import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few Args")
letters = sys.argv[1:]
print("Length is", len(letters))
number =[]
i=0
for no in letters:
    number[i] = int(no)
    i+=1
print(number)


for arg in sys.argv[1:-1]:
    print(f"Hello my name is {arg}")

if __name__ == "__main__":
    main()