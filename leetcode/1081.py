# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s) -> str:
        stack = []
        d = Counter(s)
        # 栈中有的元素
        set_array = set()
        for ele in s:
            if ele not in set_array:
                while stack and stack[-1] > ele and d[stack[-1]] > 1:
                    d[stack[-1]] -= 1
                    set_array.discard(stack.pop())
                set_array.add(ele)
                stack.append(ele)
            else:
                d[ele] -= 1
        return "".join(stack)


# 和上面思路一样
# from collections import Counter
# class Solution:
#     def removeDuplicateLetters(self, s) -> int:
#         stack = []
#         d = Counter(s)
#         # 栈中有的元素
#         set_array = set()
#         for ele in s:
#             if ele not in set_array:
#                 while stack and stack[-1] > ele and d[stack[-1]]:
#                     set_array.discard(stack.pop())
#                 set_array.add(ele)
#                 stack.append(ele)
#             # 每遍历到一个元素,该元素剩余数少1
#             d[ele] -= 1
#         return "".join(stack)

# 类似
# class Solution:
#     def smallestSubsequence(self, text: str) -> str:
#         s = set()
#         stack = []
#         for i in range(len(text)):
#             if text[i] not in s:
#                 while stack and stack[-1] > text[i] and stack[-1] in text[i + 1:]:
#                     s.remove(stack.pop())
#                 s.add(text[i])
#                 stack.append(text[i])
#         return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    text = "baababaaaaababbbbbbaababaababa"
    print(s.smallestSubsequence(text))