class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if len(s) <= 0:
            return ""
        dic, res, i = {}, 0, -1
        result = ""
        for j in range(len(s)):
            if s[j] in dic:
                # i表示结果字符串左边部分
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            # 有更长的子字符串
            if j - i > res:
                res = j - i # 更新长度
                if s[i] == s[j]:
                    if i == -1:
                        result = s[i + 1: j + 1]
                    else:
                        result = s[i: j]
                else:
                    result = s[i + 1: j + 1]
        return result


if __name__ == '__main__':
    s = Solution()
    ss = "pwwkew"
    print(s.lengthOfLongestSubstring(ss))