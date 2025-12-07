import random
a = 0
b = 1
password = input("Pass?:")
while True:
    random.shuffle(password)
    ok = True
    for i in range(len(password) - 1):
        if char_type(password[i]) == char_type(password[i + 1]):
            ok = False
            break
    if ok:
        break