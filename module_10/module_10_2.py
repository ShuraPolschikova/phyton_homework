import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemy = 100
        self.day_counter = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy > 0:
            time.sleep(1)
            self.enemy -= self.power
            self.day_counter += 1
            print(f"{self.name} сражается {self.day_counter} дней, осталось {self.enemy} врагов")

        print(f"{self.name} одержал победу спустя {self.day_counter} дней!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Добро победило, все битвы окончены, до новых кровавых встреч!")