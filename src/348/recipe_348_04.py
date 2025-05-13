import threading
import time


def print_numbers(thread_name):
    for i in range(5):
        print(f"{thread_name}: {i}")
        time.sleep(1)  # 1秒待つ


def print_letters(thread_name):
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"{thread_name}: {letter}")
        time.sleep(1.5)  # 1.5秒待つ


# スレッドを作成
thread1 = threading.Thread(target=print_numbers, args=("スレッド1",), daemon=True)
thread2 = threading.Thread(target=print_letters, args=("スレッド2",), daemon=True)

# スレッドを開始
thread1.start()
thread2.start()

# スレッドの終了を待つ
# thread1.join()
# thread2.join()

print("全ての処理が終了しました。")
