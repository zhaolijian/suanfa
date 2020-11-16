class Solution:
    def __init__(self):
        self.res = 0
    def translateNum(self, num: int) -> int:
        self.solu(0, str(num))
        return self.res
    def solu(self, index, num):
        if index >= len(num) - 1:
            self.res += 1
        else:
            if num[index] != '0' and index < len(num) - 1 and int(num[index: index + 2]) < 26:
                self.solu(index + 2, num)
            self.solu(index + 1, num)


if __name__ == '__main__':
    s = Solution()
    num = 506
    print(s.translateNum(num))