import unittest

from main import get_cost, check_month, list_of_numbers

class TestMain(unittest.TestCase):
    def test_getcoast(self):
        params = (
            (9, 'Стоимость доставки: 200 руб.'),
            (10, 'Стоимость доставки: 200 руб.'),
            (11, 'Стоимость доставки: 500 руб.'),
        )
        for i, (x, expected) in enumerate(params):
            with self.subTest(i):
                result = get_cost(x)
                self.assertEqual(expected, result)


    def test_check_month(self):
        params = (
            (1, 'Зима'),
            (4, 'Весна'),
            (6, 'Лето'),
            (8, 'Лето'),
            (11, 'Осень'),
            (16, 'Некорректный номер месяца'),
        )
        for i, (x, expected) in enumerate(params):
            with self.subTest(i):
                result = check_month(x)
                self.assertEqual(expected, result)


    def test_list_of_numbers(self):
        params = (
            (1, [1]),
            (3, [1, 2, 3]),
            (4, [1, 2, 3, 4]),
            (0, []),
        )
        for i, (x, expected) in enumerate(params):
            with self.subTest(i):
                result = list_of_numbers(x)
                self.assertEqual(expected, result)