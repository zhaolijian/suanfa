class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        # 记录第一个非0值索引
        index = 0
        for i in range(4):
            if numbers[i] == 0:
                index = i + 1
            else:
                # 如果有除0外相同的数，则不可能是顺子
                if numbers[i] == numbers[i + 1]:
                    return False
        if numbers[-1] - numbers[index] < 5:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    print(s.IsContinuous(l))
