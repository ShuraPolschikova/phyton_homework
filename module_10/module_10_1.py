import threading
import time
# выполнение задания в функциях
def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range (1, word_count+1):
            file.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Время выполнения в функциях составило {end_time-start_time:.1f} секунд")

# выполнение задания в потоках
threads = []
start_time_threads = time.time()

for count, name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=(count, name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time.time()

print(f"Время выполнения с потоками составило {end_time_threads - start_time_threads:.1f} секунд")


