import time
import threading

def create_file_with_delay(filename):
    time.sleep(1)

    with open(filename, 'w') as file:
        file.write("This is a test file.")

def main():
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = threading.Thread(target=create_file_with_delay, args=(f"file_{i}.txt",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
