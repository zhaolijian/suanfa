# str = 'catsanddog'
# wordDict = ['cat', 'cats', 'and', 'sand', 'dog']
# 分割时可以重复使用字典中的单词
# 输出：
# 'cats and dog'
# 'cat sand dog'

# 方法1 没有剪枝
# class Solution:
#     def func(self, str, wordDict):
#         res = set()
#
#         def function(string, already):
#             if not string:
#                 res.add(' '.join(already))
#                 return
#             for i in range(len(string)):
#                 if string[:i + 1] in wordDict:
#                     function(string[i + 1:], already + [string[:i + 1]])
#
#         function(str, [])
#         result = list(res)
#         return result


# 方法2 剪枝
from collections import defaultdict
class Solution:
    def func(self, str, wordDict):
        res = set()

        def function(index, already):
            if index == len(str):
                res.add(' '.join(already))
                visited[str[: index]].append(already)
                return
            if str[index:] in visited:
                for ele in visited[str[index:]]:
                    res.add(' '.join(already + ele))
                return
            for i in range(index, len(str)):
                if str[index: i + 1] in wordDict:
                    function(i + 1, already + [str[index: i + 1]])

        visited = defaultdict(list)
        function(0, [])
        result = list(res)
        return result


if __name__ == '__main__':
    str = 'catsanddog'
    wordDict = ['cat', 'cats', 'and', 'sand', 'dog']
    s = Solution()
    result = s.func(str, wordDict)
    for i in result:
        print(i)