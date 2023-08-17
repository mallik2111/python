import sys
from square import square
while True:
    try:
        if len(sys.argv) == 2:
            print(square(int(sys.argv[1])))
            break
    except ValueError:
        pass
