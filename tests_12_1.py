import modul_12_1
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t = modul_12_1.Runner('Victor')
        for i in range(10):
            t.walk()
        self.assertEqual(t.distance, 50)
    def test_run(self):
        t2 = modul_12_1.Runner('Julia')
        for i in range(10):
            t2.run()
        self.assertEqual(t2.distance, 100)
    def test_challenge(self):
        t3 = modul_12_1.Runner('Anna')
        t4 = modul_12_1.Runner('Masha')
        for i in range(10):
           t3.walk()
        for i in range(10):
            t4.run()
        self.assertNotEqual(t3.distance, t4.distance)