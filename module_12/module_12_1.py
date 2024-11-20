import unittest
import module_12_1_shablon as m12

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = m12.Runner("Runner1")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    def test_run(self):
        runner = m12.Runner("Runner2")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)


    def test_challenge(self):
        runner1 = m12.Runner("Runner1")
        runner2 = m12.Runner("Runner2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)
