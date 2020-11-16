class Solution:
    # s字符串
    def isNumeric(self, s):
        sign, decimal, hasE = False, False, False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                # 字符串最后不能是e或E， e只能出现一次
                if i == len(s) - 1 or hasE:
                    return False
                hasE = True
            elif s[i] == '+' or s[i] == '-':
                # 第二次出现+-符号，则必须紧接在e之后
                if sign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                # 第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后
                if not sign and i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if i == len(s) - 1:
                    return False
                sign = True
            elif s[i] == '.':
                # e后面不能接小数点，小数点不能出现两次
                if hasE or decimal:
                    return False
                decimal = True
            elif s[i] < '0' or s[i] > '9':
                return False
        return True



if __name__ == '__main__':
    print(ord('A'))
    print(ord('a'))