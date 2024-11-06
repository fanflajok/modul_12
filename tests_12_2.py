import modul_12_2
import unittest
class TournamentTest(unittest.TestCase):
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
    def testtour1(self):
        t1 = modul_12_2.Tournament(90, *self.l1)
        u = t1.start()
        self.__class__.all_results[1] = u
        self.assertTrue(u[2] == 'Ник')
    def testtour2(self):
        t2 = modul_12_2.Tournament(90, *self.l2)
        u2 = t2.start()
        self.__class__.all_results[2] = u2
        self.assertTrue(u2[2] == 'Ник')
    def testtour3(self):
        t3 = modul_12_2.Tournament(90, *self.l3)
        u3 = t3.start()
        self.__class__.all_results[3] = u3
        self.assertTrue(u3[3] == 'Ник')