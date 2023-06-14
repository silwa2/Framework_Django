# Выведите  в консоль таблицу умножения от 2 до 9.
from tabulate import tabulate

NUMBER_X1 = 2
NUMBER_X2 = 11
NUMBER_Y1 = 2
NUMBER_Y2 = 6
NUMBER_Y3 = 10

for x in range(NUMBER_X1, NUMBER_X2):
    for y in range(NUMBER_Y1, NUMBER_Y2):
        print(f'{y} x {x:2} = {x * y:2}\t', end='     ')

    print('  ')

print(' ')

for x in range(NUMBER_X1, NUMBER_X2):
    for y in range(NUMBER_Y2, NUMBER_Y3):
        print(f'{y} x {x:2} = {x * y:2}\t', end='     ')
    print('  ')
