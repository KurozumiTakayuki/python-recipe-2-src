my_list = [1, 3, 5, 5, 8]
if (n := len(my_list)) > 3:
    print("リストの長さ：" + str(n))

# if文の外側でもnを使う
m = n + 1     # このnはどこで定義したのだろうか？