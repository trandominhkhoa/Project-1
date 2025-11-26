import random
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
namelist = input("Nhập danh sách tên học viên(cách ra bằng dấu phẩy):")

names = namelist.split(",")

for name in names:
    name = name.strip()
    username = name[:2].lower() + str(random.randint(100, 999))
    password = ''.join(random.choice(lower + upper + numbers + symbols) for _ in range(8))
    print(name, "->", username, "-", password)