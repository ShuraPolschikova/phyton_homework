import time
import multiprocessing


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
    if __name__ == "__main__":
        file_names = [f'./file {number}.txt' for number in range(1, 5)]
        processes = []
        for file_name in file_names:
            proc = multiprocessing.Process(target=read_info, args=(file_name,))
            processes.append(proc)
            proc.start()

        for proc in processes:
            proc.join()

    end_time_multi_call = time.time()
    print(f"{end_time_multi_call-start_time_multi_call:6f} (многопроцессорный)")

