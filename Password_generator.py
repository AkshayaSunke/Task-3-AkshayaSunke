import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive number.")

else:
    characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print("Generated Password:", password)