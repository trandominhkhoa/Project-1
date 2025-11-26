import random
a = 0
b = 1
password = input("Pass?:")
while True:
        if type(password[a]) is type(password[b]):
            random.shuffle(password)
        else:
            while True:
                if type(password[a+1]) is type(password[b+1]):
                    random.shuffle(password)
                else:
                    break