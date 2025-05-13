number = 5

match number:
    case 0:
        print("ゼロです")
    case 1 | 2:
        print("1か2です")
    case _:
        print("その他の数です")