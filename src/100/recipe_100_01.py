class MyList:
    def __init__(self, x, y, z, w):
        self.elements = [x, y, z, w]

    def __getitem__(self, index):
        # 指定したインデックスの要素を取得
        if 0 <= index < len(self.elements):
            return self.elements[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        # 指定したインデックスの要素を設定
        if 0 <= index < len(self.elements):
            self.elements[index] = value
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, index):
        # 指定したインデックスの要素を削除（削除された位置には None を入れる）
        if 0 <= index < len(self.elements):
            self.elements[index] = None
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        # 要素数の取得
        return len(self.elements)

    def __repr__(self):
        return f"{self.elements[0]} {self.elements[1]} {self.elements[2]} {self.elements[3]}"


# インスタンスの生成
obj = MyList(10, 20, 30, 40)

# インデックスによる要素アクセス
print(obj[0])  # 10 (xの値)
print(obj[1])  # 20 (yの値)
print(obj[2])  # 30 (zの値)
print(obj[3])  # 40 (wの値)

# 要素の変更
obj[2] = 300
print(obj)

# 要素の削除
del obj[1]
print(obj)

# 要素数の取得
print(len(obj))
