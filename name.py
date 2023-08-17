import sys
from random import shuffle

names= ["Vachu", "Samu", "Sneha","Tanu","Sanjana","Souparnika"]
shuffle(names)
for name in names:
    print(name)
if len(sys.argv) < 2:
    sys.exit("Too few Args")
elif len(sys.argv) > 2:
    sys.exit("Too Many args")

print ("My name is ", sys.argv[1])
