from decor_timetable import *
import json
n = input('Для просмотра расписания гр. 18704 введите 1: ')
if n == '1':
    lst = []
    with open('time.txt', encoding='utf-8') as f:
        for line in f.readlines():
            a = Day(json.loads(line))
            lst.append(str(a).split(', '))
    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('1 пара', '3 пара',
                                                        '2 пара', '4 пара', '5 пара'))
    print('-' *106)
    for i in lst:
        a = Lesson(i)
        print(a)
    print('-' * 106)
else:
    print('До свидания!')
