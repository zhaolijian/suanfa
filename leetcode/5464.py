class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        temp = numBottles
        while temp >= numExchange:
            a = temp // numExchange
            b = temp % numExchange
            res += a
            temp = a + b
        return res


if __name__ == '__main__':
    s = Solution()
    numBottles = 2
    numExchange = 3
    print(s.numWaterBottles(numBottles, numExchange))