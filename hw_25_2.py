import time
import random
import threading

def write_random_number(filename):
    random_number = random.randint(1, 100)

    with open(filename, 'w') as file:
        file.write(str(random_number))
    time.sleep(1)

def main():

    threads = []
    for i in range(1000):
        thread = threading.Thread(target=write_random_number, args=(f"file_{i}.txt",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")

if __name__ == "__main__":
    start_time = time.time()
    main()
