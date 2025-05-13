data = {"name": "鈴木", "age": 30}

match data:
    case {"age": 30}:
        print("このユーザーは30才です。")