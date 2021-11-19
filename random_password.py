import string
import random
import os

chars = string.ascii_letters + string.digits
print("Random Password V1.1\nMinimum length 6 characters\nMaximum length 128 characters")
while True:
    try:
        length = int(input("password length: "))
        if not 6 <= length <= 128:
            raise ValueError()
        break
    except ValueError:
        print("Error! Try again")

password = (''.join([random.choice(chars) for i in range(length)]))
print(f"Password: {password}")

save_name = str(input("Give a name to the password: "))
file_location = ('Desktop/save.txt')
with open(file_location, 'w') as save:
    with open(file_location, 'r') as read:
        lines = 0
        for line in read:
            lines += 1
    save.write(f"{lines+1}. {password} - {save_name}\n")
    print(f"This File has been saved. File location: {file_location}")
    save.close();