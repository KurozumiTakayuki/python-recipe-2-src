class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 足し算: 他のCoordオブジェクトと加算
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        # 引き算: 他のCoordオブジェクトと減算
        if isinstance(other, Coord):
            return Coord(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        # 掛け算: スカラーと掛け算
        if isinstance(scalar, (int, float)):
            return Coord(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        # 割り算: スカラーで割り算
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Coord(self.x / scalar, self.y / scalar)
        elif scalar == 0:
            raise ValueError("0除算はできません")
        return NotImplemented

    def __floordiv__(self, scalar):
        # 切り捨て除算: スカラーで切り捨て除算
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Coord(self.x // scalar, self.y // scalar)
        elif scalar == 0:
            raise ValueError("0除算はできません")
        return NotImplemented

    def __mod__(self, scalar):
        # 剰余: スカラーで剰余
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Coord(self.x % scalar, self.y % scalar)
        elif scalar == 0:
            raise ValueError("0除算はできません")
        return NotImplemented

    def __pow__(self, scalar):
        # 剰余: スカラーで累乗
        if isinstance(scalar, (int, float)):
            return Coord(self.x ** scalar, self.y ** scalar)
        return NotImplemented

    def __repr__(self):
        return f"({self.x}, {self.y})"


# 座標を初期化
c1 = Coord(2, 3)
c2 = Coord(4, 1)

# 座標の足し算
print(c1 + c2)

# 座標の引き算
print(c1 - c2)

# スカラー積
print(c1 * 3)

# スカラー除算
print(c2 / 2)

# スカラー切り捨て除算
print(c2 // 2)

# スカラー剰余
print(c1 % 2)

# スカラー累乗
print(c2 ** 2)

# 定義されていない型での演算
print(c1 ** c2)
