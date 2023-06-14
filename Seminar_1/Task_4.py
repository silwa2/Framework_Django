# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 9
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count != -1:
    number = int(input("Введите число от 0 до 1000: "))
    if number == num:
        print("Вы угадали число - это ", number)
        break
    if number < num:
        print ("Загаданное число больше ", number)
    else:
        print("Загаданное число меньше ", number)
    print(' ')
    print(f"Осталось {count} попыток")
    count -= 1
