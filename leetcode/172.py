class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 0
        while n >= 5:
            temp = n // 5
            number += temp
            n = n//5
        return number


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(25))