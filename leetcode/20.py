# 栈解决
# 栈解决
class Solution:
    def isValid(self, s: str) -> bool:
        init = {')': '(', '}': '{', ']': '['}
        stack = []
        for ele in s:
            if ele in {'(', '[', '{'}:
                stack.append(ele)
            else:
                if not stack or init[ele] != stack.pop():
                    return False
        return not stack

# 复杂度高
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '[]' in s or '{}' in s or '()' in s:
#             s = s.replace('[]', '')
#             s = s.replace('{}', '')
#             s = s.replace('()', '')
#         return s == ''


if __name__ == '__main__':
    s = Solution()
    ss = input()
    print(s.isValid(ss))
