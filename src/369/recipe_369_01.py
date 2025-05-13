from multiprocessing import Process, Array
import time

def increment_array(shared_array):
    for _ in range(50):
        # 要素を順番にインクリメント
        for i in range(len(shared_array)):
            with shared_array.get_lock():
                shared_array[i] += 1
        time.sleep(0.01)  # ダミーI/O処理

if __name__ == '__main__':
    # 長さ5の整数型配列を作成（初期値はすべて0）
    arr = Array('i', 5)

    # プロセスを作成
    processes = []
    for _ in range(2):
        p = Process(target=increment_array, args=(arr,))
        processes.append(p)
        p.start()

    # 全プロセスの終了を待機
    for p in processes:
        p.join()

    # 結果を表示
    print("共有配列の要素:", list(arr))
