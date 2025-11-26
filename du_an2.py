
import random
length = int(input("Nhập độ dài mật khẩu:"))
print("Độ dài mật khẩu là:",length)

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"

password = ""

for i in range(length):
    password += random.choice(letters + numbers + symbols)

print("Mật khẩu của bạn là:",password)


