import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == "__main__":
    file_names = [f'./file {number}.txt' for number in range(1, 5)]
    
    start_time_linear_call = time.time()
    for file_name in file_names:
        read_info(file_name)
    end_time_linear_call = time.time()
    print(f"{end_time_linear_call-start_time_linear_call:6f} (линейный)")

    start_time_multi_call = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    end_time_multi_call = time.time()
    print(f"{end_time_multi_call-start_time_multi_call:6f} (многопроцессорный)")

