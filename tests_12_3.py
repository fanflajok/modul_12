import modul_12_1
import modul_12_2
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        t = modul_12_1.Runner('Victor')
        for i in range(10):
            t.walk()
        self.assertEqual(t.distance, 50)
    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        t2 = modul_12_1.Runner('Julia')
        for i in range(10):
            t2.run()
        self.assertEqual(t2.distance, 100)
    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        t3 = modul_12_1.Runner('Anna')
        t4 = modul_12_1.Runner('Masha')
        for i in range(10):
           t3.walk()
        for i in range(10):
            t4.run()
        self.assertNotEqual(t3.distance, t4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        r = modul_12_2.Runner('Усэйн', speed = 10)
        r2 = modul_12_2.Runner('Андрей', speed=9)
        r3 = modul_12_2.Runner('Ник', speed=3)
        self.l1 = [r,r3]
        self.l2 = [r2,r3]
        self.l3 = [r,r2,r3]
    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testtour1(self):
        t1 = modul_12_2.Tournament(90, *self.l1)
        u = t1.start()
        self.__class__.all_results[1] = u
        self.assertTrue(u[2] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testtour2(self):
        t2 = modul_12_2.Tournament(90, *self.l2)
        u2 = t2.start()
        self.__class__.all_results[2] = u2
        self.assertTrue(u2[2] == 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testtour3(self):
        t3 = modul_12_2.Tournament(90, *self.l3)
        u3 = t3.start()
        self.__class__.all_results[3] = u3
        self.assertTrue(u3[3] == 'Ник')