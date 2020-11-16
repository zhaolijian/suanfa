from collections import Counter, defaultdict
# 方法1
class Solution(object):
    def partitionLabels(self, S):
        # 当有一个key对应多个value时，后者会覆盖前者，则保留大的索引
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            # 不断更新到当前遍历位置字符的最后出现位置
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


# 方法2
# class Solution:
#     def partitionLabels(self, S: str):
#         init = Counter(S)
#         temp = defaultdict(int)
#         res = []
#         start = 0
#         for i in range(len(S)):
#             # 判断子串是否拥有了字符串中所有的元素
#             flag = True
#             temp[S[i]] += 1
#             for ele in temp.keys():
#                 if temp[ele] != init[ele]:
#                     flag = False
#                     break
#             if flag:
#                 res.append(i - start + 1)
#                 start = i + 1
#                 temp = defaultdict(int)
#         return res


if __name__ == '__main__':
    s = Solution()
    S = "ababcbacadefegdehijhklij"
    print(s.partitionLabels(S))