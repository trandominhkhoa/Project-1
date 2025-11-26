import random

lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

length = int(input("length?:"))
password_char = []
password_char.append(random.choice(numbers))   
password_char.append(random.choice(symbols))
password_char.append(random.choice(lower))   
password_char.append(random.choice(upper))  

for i in range(length - 4):
        password_char.append(random.choice(lower + upper + numbers + symbols))

random.shuffle(password_char)

password = "".join(password_char)

print("Mật khẩu là", password)