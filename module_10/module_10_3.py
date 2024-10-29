import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for trans in range(100):
            diff = random.randint(50, 500)
            with self.lock:
                self.balance += diff
                print(f"Пополнение: {diff}. Баланс: {self.balance}.")
                if self.balance >= 500 and not self.lock.locked():
                    pass
            time.sleep(0.001)

    def take(self):
        for trans in range(100):
            diff = random.randint(50, 500)
            print(f"Запрос на {diff}")
            with self.lock:
                if diff <= self.balance:
                    self.balance -= diff
                    print(f"Снятие: {diff}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
