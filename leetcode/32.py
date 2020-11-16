# 方法1，两次遍历，防止(()和())情况，时间复杂度O(n)
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) <= 1:
#             return 0
#         left = 0
#         right = 0
#         max_length = 0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 left += 1
#             else:
#                 right += 1
#             if left == right:
#                 max_length = max(max_length, 2 * left)
#             if right > left:
#                 left = right = 0
#         l, r = 0, 0
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == '(':
#                 l += 1
#             else:
#                 r += 1
#             if l == r:
#                 max_length = max(max_length, 2 * l)
#             if l > r:
#                 l = r = 0
#         return max_length


# 方法2 栈 时间复杂度和空间复杂度都为O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                # 说明)数量比(多
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans


if __name__ == '__main__':
    s = Solution()
    ss = input()
    print(s.longestValidParentheses(ss))