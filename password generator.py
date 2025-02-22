import random
chars = "abcdefghijlmnopqrstuvwxyz1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+"
length = int(input("enter length: "))
password =""

for a in range(length):
    password += random.choice(chars)
print(password)
