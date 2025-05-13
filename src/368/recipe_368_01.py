from multiprocessing import Process, Value
import time


def increment(shared_counter):
    for _ in range(50):
        with shared_counter.get_lock():  # ロックを取得して排他制御
            shared_counter.value += 1  # 値をインクリメント
        time.sleep(0.01)  # ダミーI/O処理


if __name__ == '__main__':

    # 共有変数を作成
    counter = Value('i', 0)  # 整数型の共有変数を初期値0で作成

    # プロセスを作成
    processes = []
    for _ in range(2):
        process = Process(target=increment, args=(counter,))
        processes.append(process)
        process.start()

    # 全プロセスの終了を待機
    for process in processes:
        process.join()

    # 結果を表示
    print(f"カウンタの値: {counter.value}")
