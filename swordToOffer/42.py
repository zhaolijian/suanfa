# 滑动窗口思想
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        l, r = 0, len(array) - 1
        res = float('inf')
        result = []
        while l < r:
            if array[l] + array[r] == tsum:
                temp = array[l] * array[r]
                if temp < res:
                    res = temp
                    result = [array[l], array[r]]
                l += 1
                r -= 1
            elif array[l] + array[r] > tsum:
                r -= 1
            else:
                l += 1
        return result

if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    n = int(input())
    print(s.FindNumbersWithSum(l, n))