class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = length
        for i in range(length):
            # 长度为偶数
            index = 1
            while i - index + 1 >= 0 and i + index <= length - 1:
                if s[i - index + 1] != s[i + index]:
                    break
                else:
                    res += 1
                    index += 1
            index = 1
            while i - index >= 0 and i + index <= length - 1:
                if s[i - index] != s[i + index]:
                    break
                else:
                    res += 1
                    index += 1
        return res
    

if __name__ == '__main__':
    s = Solution()
    ss = "fdsklf"
    print(s.countSubstrings(ss))