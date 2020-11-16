# class StockSpanner:
#     def __init__(self):
#         self.stock = []
#         self.result = 0
#
#     def next(self, price: int) -> int:
#         length = len(self.stock)
#         self.stock.insert(length, price)
#         for i in range(length+1):
#             if self.stock[i] > price:
#                 break
#             else:
#                 self.result += 1
#         return self.result
# 为啥上述不行？？？？？？


class StockSpanner:
    """
    用一个栈来存储过去股票的价格和对应的跨度，
    如果当天的股票价格大于栈顶的股票价格，则出栈，
    将对应的跨度加到今日股票价格的跨度上．
    直到栈顶的股票价格大于当日股票价格，然后将当日股票价格和对应的跨度入栈
    """
    def __init__(self):
        self.his_prices = [(-1, 0)]

    def next(self, price: int) -> int:
        span = 1
        while self.his_prices:
            if self.his_prices[-1][0] <= price:
                span += self.his_prices.pop(-1)[1]
            else:
                break
        self.his_prices.append((price, span))
        return span


if __name__ == '__main__':
    obj = StockSpanner()
    param_1 = obj.next(100)
    print(param_1)