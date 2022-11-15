import sort as S
from random import *
from timeit import *

dev = True
if dev:
    n = 9
    a = []
    for i in range(n):
        a.append(randint(1, 99))
else:
    stop, a = False, []
    while not(stop):
        k = input('Введите элемент списка, для остановки ввода введите S \n')
        if k in 'Ss':
            stop = True
            continue
        else:
            a.append(int(k))

k = input("Выберите метод сортировки: 1 - Быстрая, 2 - Расчёской, 3 - Блочная, 4 - Пирамидальная \n")
print(a)
if k == '1':
    start = default_timer()
    print(S.quick_sort(a))
    time = default_timer() - start
    print(f"Время быстрой сортировки {time}")
if k == '2':
    start = default_timer()
    print(S.hairbrush(a))
    time = default_timer() - start
    print(f"Время сортировки расчёской {time}")
if k == '3':
    start = default_timer()
    print(S.bucket_sort(a))
    time = default_timer() - start
    print(f"Время блочной сортировки {time}")
if k == '4':
    b = a
    start = default_timer()
    S.heap_sort(a)
    print(a)
    time = default_timer() - start
    print(f"Время сортировки расчёской {time}")
