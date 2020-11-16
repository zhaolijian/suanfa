

# 分桶
class Solution:
    def FirstNotRepeatingChar(self, s):
        # 需要区分大小写
        init = [[] for i in range(52)]
        res = []
        for i in range(len(s)):
            if s[i] >= 'a' and s[i] <= 'z':
                init[ord(s[i]) - 71].append(i)
            if s[i] >= 'A' and s[i] <= 'Z':
                init[ord(s[i]) - 65].append(i)
        for j in range(52):
            if len(init[j]) == 1:
                res.append(init[j][0])
        if not res:
            return -1
        return min(res)


if __name__ == '__main__':
    s = Solution()
    ss = input()
    print(s.FirstNotRepeatingChar(ss))
