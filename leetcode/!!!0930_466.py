# class Solution:
#     def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
#         S1 = s1 * n1
#         S2 = s2 * n2
#         index_1 = 0
#         index_2 = 0
#         len_2 = len(S2)
#         result = 0
#         curr_2 = S2[0]
#         if n1 > 0:
#             while S1:
#                 if S1[index_1] == curr_2:
#                     if index_2 == len_2-1:
#                         index_2 = 0
#                         result += 1
#                     else:
#                         index_2 += 1
#                     curr_2 = S2[index_2]
#                 S1 = S1[index_1 + 1:]
#         return result


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 找出S1子集和S2子集最小匹配处，计算出S1有多少个最小子集，S2有多少个最小子集
        


if __name__ == '__main__':
    s = Solution()
    result = s.getMaxRepetitions('lovelive', 100000, 'lovelive', 100000)
    print(result)