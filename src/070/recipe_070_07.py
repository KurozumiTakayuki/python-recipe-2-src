data = {"name": "鈴木", "age": 30}

match data:
    case {"name": name as n, "age": 30}:
        print("このユーザーは30才です。")
        print(f"名前は{name}です。")
        print(f"名前は{n}です。")