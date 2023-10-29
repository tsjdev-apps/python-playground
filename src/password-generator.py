import string
import random

length = int(input("Enter the length of your desired password: "))
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(random.choice(characters) for x in range(length))

print(password)