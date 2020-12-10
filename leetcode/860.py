# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
# 顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
# 注意，一开始你手头没有任何零钱。
# 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。


from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills) -> bool:
        d = defaultdict(int)
        for ele in bills:
            d[ele] += 1
            if ele == 10:
                if d[5] > 0:
                    d[5] -= 1
                else:
                    return False
            elif ele == 20:
                number = 15
                if d[10] >= 1:
                    d[10] -= 1
                    number -= 10
                if d[5] >= number // 5:
                    d[5] -= number // 5
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    bills = [5,5,10,10,20]
    print(s.lemonadeChange(bills))