# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 方法1 dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_3 != len_1 + len_2:
            return False
        if s3 == s1 or s3 == s2:
            return True
        dp = [[False for i in range(len_2 + 1)] for j in range(len_1 + 1)]
        dp[0][0] = True
        for i in range(1, len_1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len_2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


# 超时
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         def func(index1, index2, index3):
#             nonlocal res
#             if index1 == len1 and index2 == len2 and index3 == len3:
#                 res = True
#                 return
#             for i in range(len1 - index1):
#                 if s1[index1 + i] != s3[index3 + i]:
#                     break
#                 else:
#                     func(index1 + i + 1, index2, index3 + i + 1)
#             for j in range(len2 - index2):
#                 if s2[index2 + j] != s3[index3 + j]:
#                     break
#                 else:
#                     func(index1, index2 + j + 1, index3 + j + 1)
#
#         res = False
#         len1, len2, len3 = len(s1), len(s2), len(s3)
#         if len3 != len1 + len2:
#             return False
#         func(0, 0, 0)
#         return res


if __name__ == '__main__':
    s = Solution()
    # s1, s2, s3 = "cacabcbaccbbcbb", "acaaccaacbbbabbacc", "accacaabcbacaccacacbbbbcbabbbbacc"
    s1 = "aa"
    s2 = "ab"
    s3 = "abaa"
    print(s.isInterleave(s1, s2, s3))