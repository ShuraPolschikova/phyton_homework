# task 1
def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params()
print("*", 0, "*")
print(9, "не строка", False)
print("проверка", None, 9)
print_params(b = 25)
print_params(c = [1, 2, 3])

# task 2
values_list = ("1 элемент", [2, "э", "л", "е", "м", "е", "н", "т"], 3)
value_dict = {"a": "1 элемент", "b": False, "c": 3}

print_params(*values_list)
print_params(**value_dict)

# task 3
values_list_2=("007", False)
print_params(*values_list_2,42)