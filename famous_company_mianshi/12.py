# 给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
# 括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
class Solution:
    def isValid(self , s):
        stack = []
        set_array = {'(', '{', '['}
        init = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in set_array:
                stack.append(s[i])
            else:
                if stack and stack[-1] == init[s[i]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


if __name__ == '__main__':
    s = Solution()
    ss = '['
    print(s.isValid(ss))