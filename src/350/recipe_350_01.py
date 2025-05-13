import threading
import time

# 数字を出力するスレッドクラス
class NumberPrinterThread(threading.Thread):
    def __init__(self, thread_name):
        super().__init__()
        self.thread_name = thread_name

    def run(self):
        for i in range(5):
            print(f"{self.thread_name}: {i}")
            time.sleep(1)  # 1秒待つ

# アルファベットを出力するスレッドクラス
class LetterPrinterThread(threading.Thread):
    def __init__(self, thread_name):
        super().__init__()
        self.thread_name = thread_name

    def run(self):
        for letter in ['A', 'B', 'C', 'D', 'E']:
            print(f"{self.thread_name}: {letter}")
            time.sleep(1.5)  # 1.5秒待つ

# スレッドを作成
thread1 = NumberPrinterThread("スレッド1")
thread2 = LetterPrinterThread("スレッド2")

# スレッドを開始
thread1.start()
thread2.start()

# スレッドの終了を待つ
thread1.join()
thread2.join()

print("全ての処理が終了しました。")
