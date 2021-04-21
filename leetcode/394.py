class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele == ']':
                temp = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                number = ""
                while stack and '0' <= stack[-1] <= '9':
                    number += stack.pop()
                number = number[::-1]
                number = int(number)
                temp = temp[::-1]
                stack += number * temp
            else:
                stack.append(ele)
        return "".join(stack)

    
class Solution:
    # 碰到[,数字和之前字符串入栈，碰到]，数字和之前字符串出栈
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([res, multi])
                res, multi = "", 0
            elif c == ']':
                last_res, number = stack.pop()
                res = last_res + number * res
            else:
                res += c
        return res


if __name__ == '__main__':
    s = Solution()
    ss = "3[a2[c]]"
    print(s.decodeString(ss))
