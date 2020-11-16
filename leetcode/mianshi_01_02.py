# 判定是否互为字符重排,即两个字符串中的字母重新排列后是否能一样
# 方法1 转换成数组中sort
# class Solution:
#     def CheckPermutation(self, s1: str, s2: str) -> bool:
#         array_1, array_2 = [], []
#         for i in range(len(s1)):
#             array_1.append(ord(s1[i]))
#         for i in range(len(s2)):
#             array_2.append(ord(s2[i]))
#         len_1, len_2 = len(array_1), len(array_2)
#         if len_1 != len_2:
#             return False
#         array_1.sort()
#         array_2.sort()
#         for i in range(len_1):
#             if array_1[i] != array_2[i]:
#                 return False
#         return True


# 方法2 使用collections.Counter()方法，一行解决
# import collections
# class Solution:
#     def CheckPermutation(self, s1: str, s2: str) -> bool:
#         return collections.Counter(s1) == collections.Counter(s2)


# 方法3 使用位运算 对于相同位数的字符串，除非每个字母的数量一样，否则和不想等
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        length_1 = len(s1)
        if length_1 != len(s2):
            return False

        result = 0
        for i in range(length_1):
            result += 1 << (ord(s1[i]) - ord('a'))
            result -= 1 << (ord(s2[i]) - ord('a'))

        return result == 0


if __name__ == '__main__':
    s = Solution()
    s1 = "acf"
    s2 = "bce"
    print(s.CheckPermutation(s1, s2))