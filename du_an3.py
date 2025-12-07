import random
print("Bạn có muốn mật khẩu an toàn không?")
print("1. Có", "2. Không")

while True:
    user_req = input("Lựa chọn: ")

    if user_req.isdigit():
        requirements = int(user_req)

        if requirements in (1, 2):
            break
        else:
            print("Lựa chọn không tồn tại, thử lại.")
    else:
        print("Bạn phải nhập số!")

if requirements == 1:
    length = input("Vui lòng nhập độ dài mật khẩu mà lớn hơn 4: ")

    while True:
        if length.isdigit():
            length = int(length)

            if length <= 4:
                print("Độ dài quá ngắn, xin nhập lại.")
                length = input("Vui lòng nhập độ dài mật khẩu mới mà lớn hơn 4: ")
                continue
            else:
                break
        else:
            print("Bạn phải nhập số")
            length = input("Vui lòng nhập độ dài mật khẩu mới mà lớn hơn 4: ")

    print("Bạn đã nhập độ dài:", length)

elif requirements == 2:
    print("Bạn đã chọn không tạo mật khẩu an toàn.")

lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""
import random

a = 0
b = 1
if requirements == 1:
    password_char = []
    password_char.append(random.choice(numbers))   
    password_char.append(random.choice(symbols))
    password_char.append(random.choice(lower))   
    password_char.append(random.choice(upper))  
    for i in range(length - 4):
        password_char.append(random.choice(lower + upper + numbers + symbols,))

    random.shuffle(password_char)

    while True:
        random.shuffle(password_char)
        isPw = True
        for i in range(1,len(password_char)):
            ch1 = password_char[i-1]
            ch2 = password_char[i]

            if ch1 in lower:
                t1 = "lower"
            elif ch1 in upper:
                t1 = "upper"
            elif ch1 in numbers:
                t1 = "digit"
            else:
                t1 = "symbol"
            
            if ch2 in lower:
                t2 = "lower"
            elif ch2 in upper:
                t2 = "upper"
            elif ch2 in numbers:
                t2 = "digit"
            else:
                t2 = "symbol"
            
            if t1 == t2:
                isPw = False
                break

        if isPw:
            break

    password = "".join(password_char)
    print("Mật khẩu là", password)

else:
    length = int(input("Vui lòng nhập độ dài mật khẩu:" ))
    password += "".join(random.choices(upper + lower + numbers + symbols,k=length))
    print("Mật khẩu bạn là:", password)




