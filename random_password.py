import string
import random

chars = string.ascii_letters + string.digits
print("Рандомный пароль V1.0")
while True:
    try:
        length = int(input("Длина пароля: "))
        if length > 128:
            print("Максимальная длина пароля 128 символов")
            length = int(input("Длина пароля: "))
    except:
        print("Ошибка! Попробуйте снова")
    else:
        break
password = (''.join([random.choice(chars) for i in range(length)]))
print(f"Пароль: {password}")