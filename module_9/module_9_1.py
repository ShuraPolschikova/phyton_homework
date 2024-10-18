def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

def min(int_list):
    min = int_list[0]
    if all(isinstance(params, (int, float)) for params in int_list):
        for number in int_list:
            if number < min:
                min = number
        return min

def max(int_list):
    max = int_list[0]
    if all(isinstance(params, (int, float)) for params in int_list):
        for number in int_list:
            if number > max:
                max = number
        return max

def lenght(int_list):
    if all(isinstance(params, (int, float)) for params in int_list):
        return len(int_list)

def sum(int_list):
    result = 0
    if all(isinstance(params, (int, float)) for params in int_list):
        for number in int_list:
            result += number
        return result

def sorted(int_list):
    if all(isinstance(params, (int, float)) for params in int_list):
        for i in range(len(int_list)):
            lowest = i
            for j in range(i+1, len(int_list)):
                if int_list[j] < int_list[lowest]:
                    lowest = j
            int_list[i], int_list[lowest] = int_list[lowest], int_list[i]
        return int_list


print(apply_all_func([6, 3, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], lenght, sum, sorted))
