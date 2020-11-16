# 利用单调栈的思想解决，
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        val = 0
        while self.stack:
            temp = self.stack[-1]
            if temp[0] <= price:
                self.stack.pop()
                val += temp[1]
            else:
                break
        self.stack.append((price, val + 1))
        return val + 1