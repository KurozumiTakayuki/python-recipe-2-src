def add_unit(num: "数値", unit: "単位") -> "引数で指定された数値に単位をつけた文字列を返す":
    return str(num) + unit

text: "商品価格" = add_unit(100, "円")
