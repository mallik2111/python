def main():
    x=get_num("What is x?: ")
    print(f"value of x is {x}")

def get_num(prompt):
    while True:
        try:
            return int((input(prompt)))
        except ValueError:
                pass
    
main()