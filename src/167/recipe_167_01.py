from fractions import Fraction

# 分数の生成
fraction1 = Fraction(3, 4)  # 3/4
fraction2 = Fraction(2, 3)  # 2/3

# 四則演算
add_result = fraction1 + fraction2       # 加算
subtract_result = fraction1 - fraction2  # 減算
multiply_result = fraction1 * fraction2  # 乗算
divide_result = fraction1 / fraction2    # 除算

# 結果表示
print(f"{fraction1} + {fraction2} = {add_result}")
print(f"{fraction1} - {fraction2} = {subtract_result}")
print(f"{fraction1} * {fraction2} = {multiply_result}")
print(f"{fraction1} / {fraction2} = {divide_result}")
