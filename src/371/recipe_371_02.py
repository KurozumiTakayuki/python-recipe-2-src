from multiprocessing import Process, Queue
import time


# カウンタを増やす関数
def increment(q):
    for _ in range(50):
        value = q.get()  # キューから値を取り出し
        time.sleep(0.01)  # ダミーI/O処理
        value += 1  # インクリメント
        q.put(value)  # 更新した値を再度キューに格納


if __name__ == '__main__':

    # プロセスセーフなキューを作成
    counter_queue = Queue()
    counter_queue.put(0)  # 初期値をキューに格納

    # プロセスを作成
    processes = []
    for _ in range(2):
        process = Process(target=increment, args=(counter_queue,))
        processes.append(process)
        process.start()

    # 全プロセスの終了を待機
    for process in processes:
        process.join()

    # 結果を取得して表示
    result = counter_queue.get()
    print(f"カウンタの値: {result}")
