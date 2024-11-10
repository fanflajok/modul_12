import unittest
import modul_12_3
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(levelname)s, %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            t = modul_12_3.Runner('Victor', speed = -5)
            for i in range(10):
                t.walk()
            self.assertEqual(t.distance, 50)
            logging.info(f'test_walk" выполнен успешно {modul_12_3.Runner.walk}')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=e)
    def test_run(self):
        try:
            t2 = modul_12_3.Runner(123, speed=5)
            for i in range(10):
                t2.run()
            self.assertEqual(t2.distance, 100)
            logging.info(f'test_run" выполнен успешно {modul_12_3.Runner.run}')
        except TypeError as e2:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=e2)

if __name__ == '__name__':
    unittest.main()


