class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        length = len(s)
        res = ""
        temp = -1
        init = ['I', 'X', 'C', 'M']
        init2 = ['V', 'L', 'D']
        for i in range(length - 1, -1, -1):
            # 倍数指数
            temp += 1
            if s[i] == '4':
                res = (init[temp] + init2[temp]) + res
            elif s[i] == '9':
                res = (init[temp] + init[temp + 1]) + res
            else:
                val = int(s[i])
                temp_val = ""
                if val >= 5:
                    temp_val = init2[temp]
                    val -= 5
                temp_val += init[temp] * val
                res = temp_val + res
        return res


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    print(s.intToRoman(n))