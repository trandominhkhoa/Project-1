import random
print("Bạn có muốn mật khẩu an toàn không?")
print("1. Có","2. Không")
requirements = int(input("Lựa chọn:"))

if requirements == 1:
    length = int(input("Vui lòng nhập độ dài mật khẩu mà lớn hơn 2:" ))
    while True:
        if length < 3:
            print("Độ dài quá ngắn xin nhập lại")
            length = int(input("Vui lòng nhập độ dài mật khẩu mới mà lớn hơn 2: "))
        else:
            break


lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""
import random

if requirements == 1:
    while True:
        if length < 4:
            print("Mật khẩu bạn quá ngắn xin nhập lại")
            password = input("Vui lòng nhập mật khẩu mới: ")
        else:
            break
    
   


    password_char = []
    password_char.append(random.choice(numbers))   
    password_char.append(random.choice(symbols)) 

    for i in range(length - 2):
        password_char.append(random.choice(lower + upper + numbers + symbols))

    random.shuffle(password_char)

    password = "".join(password_char)

    print("Mật khẩu là", password)

else:
    length = int(input("Vui lòng nhập độ dài mật khẩu:" ))
    password += "".join(random.choices(upper + lower + numbers + symbols,k=length))
    print("Mật khẩu bạn là:", password)




