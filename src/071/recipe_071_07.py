data = range(10)
 
def f(x):
    return x**2 - 1

new_list = [y for x in data if (y := f(x)) > 1]
# [3, 8, 15, 24, 35, 48, 63, 80]