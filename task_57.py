# 1. Написать функцию которая находит общие элементы из 2-х списков. Написать для неё тесты.
#
# 2. Написать функцию которая удаляет дубли в списках.  Написать для неё тесты.

import unittest
import random
from unittest.mock import Mock


def test_fn1(ls, divisor):
    result = []
    idx = 0
    while idx < len(ls):
        result.append(ls[idx] / divisor)
        idx = idx + 1
    return result


def test_fn2():
    divisor = random.randint(1, 10)
    print(divisor)
    return divisor


class Tests(unittest.TestCase):
    def test_1(self):
        result = test_fn1([4, 8, 12, 16], 2)
        print(result)
        self.assertTrue(result == [2.0, 4.0, 6.0, 8.0])

    def test_2(self):
        result = test_fn1([3, 9, 12, 15], 3)
        print(result)
        self.assertTrue(result == [1.0, 3.0, 4.0, 5.0])

    def test_3(self):
        test_fn2 = Mock(return_value=3)
        result = test_fn1([3, 9, 12, 15], test_fn2())
        print(result)
        self.assertTrue(result == [1.0, 3.0, 4.0, 5.0])
