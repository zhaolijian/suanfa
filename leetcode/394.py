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
