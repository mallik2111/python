import re
email = input("Enter your mail id  ").strip()
#username, domain = email.split("@")
#if username and domain.endswith(".edu"):
#    print ("Valid")
#else:
 #   print("Invlaid")
#if re.search(r"^\w+@\w+\.(edu|com|in)$", email):
if re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", email):
    print("Valid")
else:
    print("Invalid")