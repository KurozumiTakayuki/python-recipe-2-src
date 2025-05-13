numbers = (10, 20)

match numbers:
    case (1, 2):
        print("値は1, 2です")
    case (x, y):
        print(f"値は{x}, {y}です")