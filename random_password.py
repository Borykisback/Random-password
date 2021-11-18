import string
import random

chars = string.ascii_letters + string.digits
print("Рандомный пароль V1.0\nМинимальная длина пароля 6 символов\nМаксимальная длина пароля 128 символов")
while True:
    try:
        length = int(input("Длина пароля: "))
        if not 6 <= length <= 128:
            raise ValueError()
        break
    except ValueError:
        print("Ошибка! Попробуйте снова")

password = (''.join([random.choice(chars) for i in range(length)]))
print(f"Пароль: {password}")

save_input = input("Дайте название паролю: ")

with open('save.txt', 'r') as read_file:
    data = read_file.read()

with open('save.txt', 'w') as save:
    save.write(data + "\n" + password + " - " + save_input)