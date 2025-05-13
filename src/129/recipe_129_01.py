import argparse

parser = argparse.ArgumentParser(description="2数を指定した演算子で計算します")

parser.add_argument("num1", help="1番目の数値を指定してください。", type=float)
parser.add_argument("num2", help="2番目の数値を指定してください。", type=float)
parser.add_argument("--operator", help="演算子（+、-、*、/）を指定してください。省略したりそれ以外を指定すると足し算になります。", default="+", type=str)
args = parser.parse_args()

print(args.num1)
print(args.num2)
print(args.operator)

if args.operator in ["+", "-", "*", "/"]:
    operator = args.operator
else:
    operator = "+"

expression = " ".join([str(args.num1), operator, str(args.num2)])
print(expression, "=", eval(expression))
