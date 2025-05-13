numbers = [1, 2, 3, 4]

match numbers:
    case [x, *rest]:
        print(f"x = {x}, 残り = {rest}")