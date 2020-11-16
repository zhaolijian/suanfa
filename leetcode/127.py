# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。

# 说明:
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。


# 方法1 双向bfs
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_list = set(wordList)
        if not wordList or endWord not in set_list:
            return 0
        visited = {beginWord, endWord}
        left, right = {beginWord}, {endWord}
        number = 0
        length = len(beginWord)
        # 当前层中数量少的给left,多的给right
        while left:
            number += 1
            next_level = set()
            for word in left:
                for j in range(length):
                    for m in range(26):
                        new_word = word[:j] + chr(ord('a') + m) + word[j + 1:]
                        if new_word in right:
                            return number + 1
                        if new_word not in visited and new_word in set_list:
                            visited.add(new_word)
                            next_level.add(new_word)
            left = next_level
            if len(left) > len(right):
                left, right = right, left
        return 0



# 方法2 单向bfs，时间复杂度O(n * m * 26)  n为数组长度，m为单词长度
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        set_list = set(wordList)
        if not wordList or endWord not in set_list:
            return 0
        length = len(beginWord)
        visited = set()
        visited.add(beginWord)
        array = [beginWord]
        number = 0
        while array:
            number += 1
            new_array = []
            for i in range(len(array)):
                word = array.pop()
                for i in range(length):
                    for j in range(26):
                        new_word = word[:i] + chr(j + ord('a')) + word[i + 1:]
                        if new_word in set_list and new_word not in visited:
                            if new_word == endWord:
                                return number + 1
                            new_array.append(new_word)
                            visited.add(new_word)
            array = new_array
        return 0





# 方法3 单向bfs
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
#         # 两个单词是否只差最多一个字母
#         def diff(word1, word2):
#             length = len(word1)
#             number = 0
#             for i in range(length):
#                 if word1[i] != word2[i]:
#                     number += 1
#                     if number > 1:
#                         return False
#             return True
#
#         if endWord not in wordList:
#             return 0
#         visited = set()
#         visited.add(beginWord)
#         array = [(beginWord, 1)]
#         while array:
#             new_array = []
#             # 注意这一定要这样写，不能像下面一样那么写，下面那并不是bfs，深度可能会增加
#             for i in range(len(array)):
#                 temp = array.pop()
#                 cur_word, number = temp[0], temp[1]
#                 for ele in wordList:
#                     if ele not in visited and diff(cur_word, ele):
#                         if ele == endWord:
#                             return number + 1
#                         else:
#                             visited.add(ele)
#                             new_array.append((ele, number + 1))
#             array = new_array
#         return 0



# 错误代码
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
#         # 两个单词是否只差最多一个字母
#         def diff(word1, word2):
#             length = len(word1)
#             number = 0
#             for i in range(length):
#                 if word1[i] != word2[i]:
#                     number += 1
#                     if number > 1:
#                         return False
#             return True
#
#         if endWord not in wordList:
#             return 0
#         visited = set()
#         visited.add(beginWord)
#         array = [(beginWord, 1)]
#         while array:
#             这不能这么写，要用for循环，这不是bfs了
#             temp = array.pop()
#             cur_word, number = temp[0], temp[1]
#             for ele in wordList:
#                 if ele not in visited and diff(cur_word, ele):
#                     if ele == endWord:
#                         return number + 1
#                     else:
#                         visited.add(ele)
#                         array.append((ele, number + 1))
#         return 0


if __name__ == '__main__':
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(s.ladderLength(beginWord, endWord, wordList))