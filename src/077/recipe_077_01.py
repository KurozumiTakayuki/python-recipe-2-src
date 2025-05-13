# 位置専用パラメータを使った関数
def add_numbers(param1, param2, /, opt=0):
    result =  param1 + param2 + opt
    print(result)

# 全て位置引数で呼び出し
add_numbers(1, 2, 3)

# optのみキーワード引数を指定
add_numbers(1, 2, opt=3)

# 全てキーワード引数で呼び出し（エラー発生）
add_numbers(param1=1, param2=2, opt=3)