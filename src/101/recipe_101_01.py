class MyCounter:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # イテレーター自身（self）を返す
        return self

    def __next__(self):
        # currentが1以上なら次の要素として返し、currentを1 減らす
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            # 0 以下になったら繰り返しを終了させるためにStopIteration例外を送出
            raise StopIteration


# MyCounterを生成
obj = MyCounter(5)

# for 文で要素を順番に取得
for num in obj:
    print(num)
