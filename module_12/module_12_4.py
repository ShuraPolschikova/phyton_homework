import logging
import unittest
import module_12_1_shablon as m12

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w", encoding="UTF-8",
                    format="%(asctime)s:| %(levelname)s: | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if speed < 0:
            raise ValueError("Скорость не может быть <0")
        if not isinstance(name, str):
            raise TypeError("Имя бегуна введено неверно")
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = m12.Runner("Runner1")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        logging.info('"test_walk" выполнен успешно')


    def test_run(self):
        runner = m12.Runner("Runner2")
        for i in range(10):
                runner.run()
        self.assertEqual(runner.distance, 100)
        logging.info('"test_run" выполнен успешно')


    def test_challenge(self):
        runner1 = m12.Runner("Runner1")
        runner2 = m12.Runner("Runner2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


try:
    first = Runner('Вося', -10)
except ValueError as e:
    logging.warning(f"Ошибка параметров Runner: {e}")
    logging.exception("А вот и подробности ошибки")

second = Runner('Илья', 5)
try:
    third = Runner(43535, 10)
except TypeError as e:
    logging.warning(f"Ошибка параметров Runner: {e}")
    logging.exception("А вот и подробности ошибки")


t = Tournament(101, second)
print(t.start())
