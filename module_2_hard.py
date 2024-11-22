import random

first = random.randrange(3, 21)
print(f'Число в первом поле: {first}')
passw = ''
for i in range(1, first):
    for j in range(i, first):
        if i == j:
            continue
        if first % (i + j) == 0:
            if j < 10:
                password = i * 10 + j
            elif j >= 10 and j < 100:
                password = i * 100 + j
            a = str(password)
            passw = passw + a
        else:
            continue
password = int(passw)

print(f'Пароль: {password}')