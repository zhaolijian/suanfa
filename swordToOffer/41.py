# 这种方法本地编译器和牛客网输出不一样，本地结果正确的
# class Solution:
#     def FindContinuousSequence(self, tsum):
#         if tsum <= 2:
#             return []
#         res = []
#         n = 2
#         while n < pow(2 * tsum, 0.5):
#             temp = []
#             # 分成的份数为奇数
#             if n % 2 == 1:
#                 if (tsum / n) % 1 != 0 or tsum // n - (n // 2) < 1:
#                     n += 1
#                     continue
#                 t = tsum // n - (n // 2)
#                 for i in range(n):
#                     temp.append(t)
#                     t += 1
#                 res.append(temp)
#             # 分成的份数为偶数
#             else:
#                 if (tsum / n) % 1 != 0.5 or tsum // n - (n // 2) < 0:
#                     n += 1
#                     continue
#                 t = tsum // n - (n // 2) + 1
#                 for i in range(n):
#                     temp.append(t)
#                     t += 1
#                 res.append(temp)
#             n += 1
#         res.reverse()
#         return res


# 滑动窗口的思想
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 2:
            return []
        res = []
        left = 1
        right = 2
        while left < right:
            temp = (left + right) * (right - left + 1) / 2
            if temp == tsum:
                sum = []
                for i in range(left, right + 1):
                    sum.append(i)
                res.append(sum)
                right += 1
            elif temp > tsum:
                left += 1
            else:
                right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    print(s.FindContinuousSequence(n))
