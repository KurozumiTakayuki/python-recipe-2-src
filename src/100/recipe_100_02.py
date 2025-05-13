class MyList:
    def __init__(self, x, y, z, w):
        self.elements = [x, y, z, w]

    def __getitem__(self, key):
        if key == 'x':
            return self.elements[0]
        elif key == 'y':
            return self.elements[1]
        elif key == 'z':
            return self.elements[2]
        elif key == 'w':
            return self.elements[3]
        else:
            raise KeyError(f"Invalid key: {key}")

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

print(obj['x']) # 辞書のように文字列のキーを指定
