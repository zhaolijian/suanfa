# 最大公约数
def max_common(self, number1, number2):
    while number1 % number2:
        number1, number2 = number2, number1 % number2
    return number2