from multiprocessing import Process
import time


def init_data():
    with open('tmp.txt', 'w') as f:
        f.write("0")


def write_data(n):
    with open('tmp.txt', 'w') as f:
        f.write(str(n))


def read_data():
    with open('tmp.txt', 'r') as f:
        text = f.read()
        return int(text)


def increment():
    for _ in range(10):
        value = read_data()
        value = value + 1
        time.sleep(0.1) # ダミーのI/O時間
        write_data(value)


if __name__ == "__main__":
    init_data()
    p1 = Process(target=increment)
    p2 = Process(target=increment)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"カウンタの値: {read_data()}")
