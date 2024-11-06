import unittest
import tests_12_3


supertest = unittest.TestSuite()
supertest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
supertest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
r = unittest.TextTestRunner(verbosity=2)
r.run(supertest)