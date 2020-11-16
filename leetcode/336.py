# class Solution:
#     def palindromePairs(self, words):
#
#         def findWord(s: str, left: int, right: int) -> int:
#             # 如果indices中不存在s[left:right + 1]，则返回-1
#             return indices.get(s[left:right + 1], -1)
#
#         def isPalindrome(s: str, left: int, right: int) -> bool:
#             temp = s[left:right + 1]
#             return temp == temp[::-1]
#
#         n = len(words)
#         indices = {word[::-1]: i for i, word in enumerate(words)}
#
#         ret = list()
#         for i, word in enumerate(words):
#             m = len(word)
#             # 考虑空串
#             for j in range(m + 1):
#                 if isPalindrome(word, j, m - 1):
#                     leftId = findWord(word, 0, j - 1)
#                     if leftId != -1 and leftId != i:
#                         ret.append([i, leftId])
#                 if j and isPalindrome(word, 0, j - 1):
#                     rightId = findWord(word, j, m - 1)
#                     if rightId != -1 and rightId != i:
#                         ret.append([rightId, i])
#
#         return ret

class Solution:
    def palindromePairs(self, words):
        # 是否是回文串
        def isPalindrome(word, start, end):
            return word[start: end + 1] == word[start: end + 1][::-1]

        def exist(word, start, end):
            return d.get(word[start: end + 1], -1)

        res = []
        d = {}
        for i, word in enumerate(words):
            d[word[::-1]] = i
        for i, word in enumerate(words):
            length = len(word)
            for j in range(length + 1):
                # 如果右侧是回文串,则判断左侧的逆字符串是否存在于d中
                if isPalindrome(word, j, length - 1):
                    val = exist(word, 0, j - 1)
                    if val != -1 and val != i:
                        res.append([i, val])
                # 如果左侧是回文串,则判断右侧的逆字符串是否存在于d中
                # 如果不加j的话，那么对于两个字母镜像对称的情况会计算两次
                # 比如abcd和dcba，当遍历到abcd时，abcd的右侧空字符串为回文串，在字典中找到dcba,则[0，1]为一个结果
                # 当遍历到dcba时，dcba的左侧空字符串为回文串，在字典中找到abcd,则[0，1]为一个结果,于是重复
                # 加j的作用是不再考虑空串
                if j and isPalindrome(word, 0, j - 1):
                    val = exist(word, j, length - 1)
                    if val != -1 and val != i:
                        res.append([val, i])
        return res



# 超时
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         length = len(words)
#         res = []
#         for i in range(length):
#             for j in range(i + 1, length):
#                 temp1 = words[i] + words[j]
#                 temp2 = words[j] + words[i]
#                 len_1, len_2 = len(temp1), len(temp2)
#                 if temp1[: len_1 // 2] == temp1[len_1 // 2:][::-1]:
#                     res.append([i, j])
#                 elif temp1[: len_1 // 2] == temp1[len_1 // 2 + 1:][::-1]:
#                     res.append([i, j])
#                 if temp2[: len_2 // 2] == temp2[len_2 // 2:][::-1]:
#                     res.append([j, i])
#                 elif temp2[: len_2 // 2] == temp2[len_2 // 2 + 1:][::-1]:
#                     res.append([j, i])
#         return res


if __name__ == '__main__':
    s = Solution()
    words = ["abcd","dcba","lls","s","sssll"]
    print(s.palindromePairs(words))