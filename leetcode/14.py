class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or (len(strs) == 1 and strs[0] == ""):
            return ""
        res = ''
        max_length = max([len(strs[i]) for i in range(len(strs))])
        for i in range(max_length):
            temp = set()
            for j in range(len(strs)):
                if len(strs[j]) > i:
                    temp.add(strs[j][i])
                else:
                    return res
            if len(temp) > 1:
                return res
            else:
                res += strs[j][i]
        return res


if __name__ == '__main__':
    strs = input()
    s = Solution()
    print(s.longestCommonPrefix(strs))