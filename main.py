import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%',  '&', '*', '-', '_','?', '/']

print('Welcome to the PyPassword Generator!')
nr_letter = int(input('How many letters would you like in your password?'))
nr_number = int(input('How many numbers would you like in your password?'))
nr_symbols = int(input('How many symbols would you like in your password?'))

nr_password = []

for char in range(1, nr_letter + 1):
    nr_password.append(random.choice(letter))
for char in range(1, nr_number + 1):
    nr_password.append(random.choice(number))
for char in range(1, nr_symbols + 1):
    nr_password.append(random.choice(symbols))

# print(nr_password)

random.shuffle(nr_password)

# print(nr_password)

password = ''
for letter in nr_password:
    password += letter

print(f'Your password is: {password}')
