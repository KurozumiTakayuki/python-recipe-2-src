import math

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        # 原点からの距離を計算
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # 比較演算子の実装
    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() == other.distance_from_origin()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() != other.distance_from_origin()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() < other.distance_from_origin()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() <= other.distance_from_origin()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() > other.distance_from_origin()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Coord):
            return self.distance_from_origin() >= other.distance_from_origin()
        return NotImplemented

    def __repr__(self):
        return f"Coord({self.x}, {self.y})"

c1 = Coord(3, 4)  # 原点からの距離は5
c2 = Coord(6, 8)  # 原点からの距離は10

# 距離による比較演算
print(c1 == c2)  # False
print(c1 != c2)  # True
print(c1 < c2)   # True
print(c1 <= c2)  # True
print(c1 > c2)   # False
print(c1 >= c2)  # False
