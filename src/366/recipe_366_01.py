import multiprocessing
import time


def print_numbers(process_name):
    for i in range(5):
        print(f"{process_name}: {i}")
        time.sleep(1)  # 1秒待つ


def print_letters(process_name):
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"{process_name}: {letter}")
        time.sleep(1.5)  # 1.5秒待つ


if __name__ == '__main__':

    # プロセスを作成
    process1 = multiprocessing.Process(target=print_numbers, kwargs={"process_name": "プロセス1"})
    process2 = multiprocessing.Process(target=print_letters, args=("プロセス2",))

    # プロセスを開始
    process1.start()
    process2.start()

    while process1.is_alive() and process2.is_alive():
        print("Process1、Process2共に実行中")
        time.sleep(1)

    # プロセスの終了を待つ
    process1.join()
    process2.join()

    print("全ての処理が終了しました。")
