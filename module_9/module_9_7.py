def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)

        if result == 0:
            print("Число 0 не является ни простым, ни составным")
            return result
        elif result == 1:
            print("Число 1 не является ни простым, ни составным")
            return result
        elif result >= 2:
            for i in range(2, result):
                if result % i == 0:
                    print("Составное")
                    return result
                else:
                    print("Простое")
                    return result
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)

