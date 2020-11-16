class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        length = len(s)
        res = ""
        circle = 2 * numRows - 2
        for i in range(numRows):
            if i == 0:
                temp = 0
                while circle * temp < length:
                    res += s[circle * temp]
                    temp += 1
            elif i == numRows - 1:
                temp = 0
                while circle * temp + numRows - 1 < length:
                    res += s[circle * temp + numRows - 1]
                    temp += 1
            else:
                res += s[i]
                temp = 1
                while circle * temp + i < length:
                    res += s[circle * temp - i]
                    res += s[circle * temp + i]
                    temp += 1
                if circle * temp - i < length:
                    res += s[circle * temp - i]
        return res



if __name__ == '__main__':
    s = Solution()
    ss = input()
    n = int(input())
    print(s.convert(ss, n))