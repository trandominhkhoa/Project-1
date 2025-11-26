lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

points = 0

password = input("Nhập mật khẩu: ")

for ch in password:
    if ch in lower:
        points += 1
    elif ch in upper:
        points += 1
    elif ch in numbers:
        points += 3
    elif ch in symbols:
        points += 2
    else:
        points += 0  

if points >= 8:
    print("Mật khẩu của bạn mạnh")
else:
    print("Mật khẩu của bạn yếu")


