import unittest
import module_12_2_shablon as m12


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = m12.Runner("Усэйн", 10)
        self.runner2 = m12.Runner("Андрей", 9)
        self.runner3 = m12.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f"{name}: {result}")

    def test_Usain_Nik(self):
        tournament = m12.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertEqual(list(results.values())[-1].name, "Ник")

    def test_Andrei_Nik(self):
        tournament = m12.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertEqual(list(results.values())[-1].name, "Ник")

    def test_all_runner(self):
        tournament = m12.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertEqual(list(results.values())[-1].name, "Ник")
