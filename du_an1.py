length = int(input("Vui lòng nhập độ dài mật khẩu mà lớn hơn 2:" ))
while True:
    if length < 3:
            print("Độ dài quá ngắn xin nhập lại")
            length = int(input("Vui lòng nhập độ dài mật khẩu mới (Lớn hơn 2): "))
    else:
         break
import random
password_number = int(input("Vui lòng nhập số mật khẩu cần tạo: "))


lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if password_number > 1:
    print("Các mật khẩu là:")
else:
     print("Mật khẩu là")
for e in range(password_number):
    password_char = []

    password_char.append(random.choice(numbers))   
    password_char.append(random.choice(symbols)) 

    for i in range(length - 2):
        password_char.append(random.choice(lower + upper + numbers + symbols))

    random.shuffle(password_char)

    password = "".join(password_char)

    print(password)


