# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
#（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        array = list(str(N))
        length = len(array)
        i = 1
        # 找到第一个前面值比后面值大的位置
        while i < length:
            if array[i - 1] > array[i]:
                break
            i += 1
        if i < length:
            # 比如442   结果应该是399.对于连续值相等的情况和不等的情况是不一样的
            while i > 0 and array[i - 1] > array[i]:
                array[i - 1] = chr(ord(array[i - 1]) - 1)
                i -= 1
            for k in range(i + 1, length):
                array[k] = '9'
        return int(''.join(array))


if __name__ == '__main__':
    s = Solution()
    N = 10
    print(s.monotoneIncreasingDigits(N))