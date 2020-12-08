# 给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。
# 由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，
# 满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。
# 当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。
# 比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
# 如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。请注意， x + y 表示连接字符串 x 和 y 。

# 方法1 Aprefix + Bsuffix  或  Bprefix + Asuffix
# class Solution:
#     def checkPalindromeFormation(self, a: str, b: str) -> bool:
#         # Aprefix + Bsuffix,且Aprefix长度大于Bsuffix
#         def func(a, b):
#             flag = True
#             for i in range(length // 2):
#                 if flag and a[i] != b[length - i - 1]:
#                     flag = False
#                 if not flag and a[i] != a[length - i - 1]:
#                     return False
#             return True
#
#         length = len(a)
#         if func(a, b) or func(b, a):
#             return True
#         # 取逆，则对于取逆前的a,b，func(a, b)相当于Asuffix + Bprefix，且Bprefix的长度大于Asuffix
#         # func(b, a)相当于Aprefix + Bsuffix，且Asuffix的长度大于Bprefix
#         a, b = a[::-1], b[::-1]
#         if func(a, b) or func(b, a):
#             return True
#         return False


# 方法2
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # 从中间往两边找
        def func(a, b, left):
            right = length - left - 1
            while left >= 0 and right < length:
                if a[left] != b[right]:
                    return left
                left -= 1
                right += 1
            return left

        length = len(a)
        left = length // 2 - 1
        l = func(a, a, left)
        # func(a, b, l): Aprefix长度大于Bsuffer，回文字符串为Aprefix + Bsuffix的情况
        # func(b, a, l)： Aprefix长度大于Bsuffer，回文字符串为Bprefix + Asuffix的情况
        if func(a, b, l) == -1 or func(b, a, l) == -1:
            return True
        l = func(b, b, left)
        # func(b, a, l)： Bprefix长度大于Asuffer，回文字符串为Bprefix + Asuffix的情况
        # func(a, b, l): Bprefix长度大于Asuffer，回文字符串为Aprefix + Bsuffix的情况
        if func(b, a, l) == -1 or func(a, b, l) == -1:
            return True
        return False


# 和上面思想一样，感觉上面好理解些
# class Solution:
#     def checkPalindromeFormation(self, a: str, b: str) -> bool:
#         # 从中间往两边找
#         def func(a, b, left):
#             right = length - left - 1
#             while left >= 0 and right < length:
#                 if a[left] != b[right]:
#                     return left
#                 left -= 1
#                 right += 1
#             return left
#
#         length = len(a)
#         left = length // 2 - 1
#         l = min(func(a, a, left), func(b, b, left))
#         l = min(func(a, b, l), func(b, a, l))
#         return l == -1


if __name__ == '__main__':
    s = Solution()
    a = "pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    print(s.checkPalindromeFormation(a, b))