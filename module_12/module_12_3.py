import unittest
import module_12_2 as m2
import module_12_1 as m1

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase((m2.TournamentTest)))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase((m1.RunnerTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)
