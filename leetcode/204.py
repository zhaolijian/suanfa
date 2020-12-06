# 统计所有小于非负整数 n 的质数的数量。


# 方法1 超时。。。
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        flag = True
        for i in range(2, n):
            for j in range(2, int(pow(i, 0.5)) + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                res += 1
            flag = True
        return res


# 方法2 埃氏筛： 如果一个数为质数，那么它的所有大于1的倍数都为合数
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        # 质数为1， 合数为0
        isPrime = [1] * n
        for i in range(2, n):
            if isPrime[i] == 1:
                res += 1
                # 从i*i开始，因为之前的2*i,3*i在开始遍历到质数为2/3的时候已经设置过了
                j = i * i
                while j < n:
                    isPrime[j] = 0
                    j += i
        return res


if __name__ == '__main__':
    s = Solution()
    n = 1500000
    print(s.countPrimes(n))