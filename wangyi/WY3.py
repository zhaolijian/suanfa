# 小易经常沉迷于网络游戏.有一次,他在玩一个打怪升级的游戏,他的角色的初始能力值为 a.
# 在接下来的一段时间内,他将会依次遇见n个怪物,每个怪物的防御力为b1,b2,b3...bn.
# 如果遇到的怪物防御力bi小于等于小易的当前能力值c,那么他就能轻松打败怪物,并且使得自己的能力值增加bi;
# 如果bi大于c,那他也能打败怪物,但他的能力值只能增加bi 与c的最大公约数.
# 那么问题来了,在一系列的锻炼后,小易的最终能力值为多少?
class Solution:
    # 最大公约数
    def max_common(self, number1, number2):
        while number1 % number2:
            number1, number2 = number2, number1 % number2
        return number2

    def func(self, n, a, array):
        res = a
        for i in range(n):
            if array[i] <= res:
                res += array[i]
            else:
                res += self.max_common(res, array[i])
        return res


if __name__ == '__main__':
    while True:
        try:
            # 怪物数量、初始能力值
            n, a = map(int, input().split())
            array = []
            for i in range(n):
                array.append(int(input()))
            s = Solution()
            print(s.func(n, a, array))
        except:
            break