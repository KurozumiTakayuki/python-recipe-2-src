import multiprocessing
import time

# 数字を出力するプロセスクラス
class NumberPrinterProcess(multiprocessing.Process):
    def __init__(self, process_name):
        super().__init__()
        self.process_name = process_name

    def run(self):
        for i in range(5):
            print(f"{self.process_name}: {i}")
            time.sleep(1)  # 1秒待つ

# アルファベットを出力するプロセスクラス
class LetterPrinterProcess(multiprocessing.Process):
    def __init__(self, process_name):
        super().__init__()
        self.process_name = process_name

    def run(self):
        for letter in ['A', 'B', 'C', 'D', 'E']:
            print(f"{self.process_name}: {letter}")
            time.sleep(1.5)  # 1.5秒待つ

if __name__ == '__main__':
    # プロセスを作成
    process1 = NumberPrinterProcess("プロセス1")
    process2 = LetterPrinterProcess("プロセス2")

    # プロセスを開始
    process1.start()
    process2.start()

    # プロセスの終了を待つ
    process1.join()
    process2.join()

    print("全ての処理が終了しました。")
