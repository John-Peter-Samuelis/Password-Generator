import random

print("Welcome to the PyPassword Generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters   = int(input("How many letters would you like in your password?\n"))
number_of_symbols   = int(input("How many symbols would you like in your password?\n"))
number_of_numbers   = int(input("How many numbers would you like in your password?\n"))

generated_password  = ""
password = []

for character in range(1, number_of_letters+1):
    password.append(random.choice(letters))
 

for symbolstobegenerated in range(1, number_of_symbols+1):
    password.append(random.choice(symbols))

for numberstobegenerated in range(1, number_of_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)

for eachCharacter in password:
    generated_password += eachCharacter  

print(f"Password: {generated_password}")

