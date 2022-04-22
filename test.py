# Необходим при замере скорости выполнения кода
from datetime import datetime as t
# Нужен для создания словаря в алг. Бойера-Мура
from collections import defaultdict

#для пятнашек
from tabulate import tabulate
import time
from queue import PriorityQueue

N = 4

# Функция, определяющая движение пятнашек
def moves(position):
    blank = position.index(0)
    # Возвращаются значения из кортежа с целой частью и остатком
    i, j = divmod(blank, N)
    # Задаем массив из смещений
    offsets = []
    # Движение вниз
    if i > 0: offsets.append(-N)     
    # Движение вверх
    if i < N - 1: offsets.append(N)  
    # Движение вправо
    if j > 0: offsets.append(-1)
    # Движение влево
    if j < N - 1: offsets.append(1)  
    for offset in offsets:
        # Заполянем пустую ячейку элементом, который мы двигаем
        swap = blank + offset
        # Проверяем на то, является ли заменяемая ячейка пустой,
        # и в случае, если у нас есть следующий элемент (не конец),
        # то выводим ее индекс, а иначе индекс последнего элемента
        yield tuple(position[swap] if x==blank else position[blank] if x==swap else position[x] for x in range(N*N))


# Функция, определяющая есть ли у пятнашек конечное решение
def parity(permutation):
    # Создаем набор из уникальных данных с пройденными ячейками
    # и создаем кол-во циклов прохождения по массиву ячеек
    seen, cycles = set(), 0
    for i in permutation:
        # Проверяем на наличие текущей ячейки в нашем наборе при перестановке
        # и добавляем его в набор при его отсутствии в нем
        if i not in seen:
            # Наращиваем счетчик циклов при отсутствии значений в наборе
            cycles += 1
            while i not in seen:
                seen.add(i)
                i = permutation[i]
    return (cycles + len(permutation)) % 2

    # Класс, определяющий параметры заданного набора
class Position:
    # Конструктор, принимающий позицию и начальную дистанцию
    def __init__(self, position, start_distance):
        self.position = position
        self.start_distance = start_distance

    # Функция, срабатывающая при сравнении (<) объекта с другим объектом
    def __lt__(self, other):
        return self.start_distance < other.start_distance

    # Функция, срабатывающая при использовании объекта как строки
    # и создающая пятнашки в виде квадратной матрицы
    def __str__(self):
        return '\n'.join((N*'{:3}').format(*[i%(N*N) for i in self.position[i:]]) 
for i in range(0, N*N, N))

SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
start = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]

# Проверяем, можно ли в данной расстановке найти решение. Если нет, то выводим предупреждающее сообщение
if parity(start) == 0:
    print('Задачу решить нельзя')
else:
    # Иначе заполняем наш кортеж значниями из данного набора
    start = tuple(start)

    p = Position(start, 0)

    print(p)
    print()

    # Кладем в очередь с приоритетом первоначальную позицию
    candidates = PriorityQueue()
    candidates.put(p)

    # Кортеж посещенных нами позиций
    visited = set([p])
    # Словарь из позиции в качестве ключа, значение которого в дальнейшем
    # будем заполнять теми ячейками, которые стоит переместить для получения решения
    came_from = {p.position: None}

    while p.position != SOLVED:
        # Извлекаем из очереди позицию с наименьшим приоритетом
        p = candidates.get()
        # Кладем в очередь все соседние позиции. Повторяем, пока не вытащим конечную позицию из очереди
        for k in moves(p.position):
            if k not in visited:
                candidates.put(Position(k, p.start_distance + 1))
                came_from[k] = p
                visited.add(k)

    # Последовательное решение пятнашек (путь)
    path = []
    # Сохраняем конечную позицию
    prev = p
    # Идем в обратном порядке и запоминаем очередность хода в path
    while p.position != start:
        # Запоминаем, откуда ход
        p = came_from[p.position]
        number = p.position[prev.position.index(0)]
        path.append(number)
        prev = p
    path.reverse()

    print(path)