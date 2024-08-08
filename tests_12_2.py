# -*- coding: utf-8 -*-
# tests_12_2.py
import runner_and_tournament as r_
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = r_.Runner('Усэйн', 10)
        self.runner2 = r_.Runner('Андрей', 9)
        self.runner3 = r_.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('-------- Все результаты соревнований -------')
        for result1 in cls.all_results:
            one_result_dict = {}  # Буфер, для вывода как словарь
            for key, value in result1.items():
                value1 = str(value)  # Извлекаем "name"
                value1 = f'{value1:6}' # Форматирование строки
                one_result_dict[key] = value1
            print(one_result_dict)

    def test_tour1(self):
        # Андрей и Ник
        tour1 = r_.Tournament(90, self.runner2, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест

    def test_tour2(self):
        # Усэйн и Ник
        tour1 = r_.Tournament(90, self.runner1, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест

    def test_tour3(self):
        # Усэйн, Андрей и Ник
        tour1 = r_.Tournament(90, self.runner1, self.runner2, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест
