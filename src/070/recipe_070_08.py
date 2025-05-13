class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Coord(1, 2)

match point:
    case Coord(x=1):
        print("pointのx座標は1です。")