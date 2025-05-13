number = 5

match number:
    case x if x > 0:
        print(f"{x} は正の数です")
    case _:
        print("負の数かゼロです")