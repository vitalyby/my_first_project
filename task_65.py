# 1. Сделать генератор который принимает на вход число x, пусть x = 5, и возвращает 5 разных простых чисел.
# Простое число: число которое делится только на себя и на 1.
# Запустить генератор подав на вход 1 000 000, и сгенерировать с его помощью 6 простых чисел.
import random


def t65(x):
    a = []
    for _ in range(x):
        a.append(random.randint(1, 9))
    return a


print(t65(5))
print('--------------')

def lazy_fn(fn, ls):
    for x in ls:
        y = fn(x)
        yield y


generator = lazy_fn(t65, [6,3,4])
print(next(generator))
print(next(generator))
print(list(generator))
print('--------------')

# 2. Превратить генератор в итератор
class lazy_map:
    def __init__(self, fn, ls):
        self.fn = fn
        self.idx = 0
        self.ls = ls

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > len(self.ls):
            raise StopIteration()
        else:
            val = self.fn(self.ls[self.idx])
            self.idx = self.idx + 1
            return val


iterator = lazy_map(t65, [2, 3, 5, 6])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
