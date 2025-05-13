class Coord:
    """ 座標(x, y)を表すクラス """
    def __init__(self, x, y):
        self.x = x
        self.y = y

c1 = Coord(2, 3)
c2 = Coord(4, 1)
c3 = c1 <= c2
print(c3)
