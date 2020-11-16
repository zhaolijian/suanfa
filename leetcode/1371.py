class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        temp = 0
        res = 0
        # 00000-11111,数组大小设置为32即可
        init = [-1] * 32
        # init数组中的元素表示temp为某个值时包含的元素
        init[0] = 0
        for i in range(len(s)):
            if s[i] == 'a':
                temp ^= 1<<0
            elif s[i] == 'e':
                temp ^= 1<<1
            elif s[i] == 'i':
                temp ^= 1<<2
            elif s[i] == 'o':
                temp ^= 1<<3
            elif s[i] == 'u':
                temp ^= 1<<4
            if init[temp] == -1:
                # 表示temp出现的最早位置
                init[temp] = i + 1
            else:
                # 元音字母出现次数：奇数减奇数等于偶数，偶数减偶数等于偶数
                res = max(res, i + 1 - init[temp])
        return res


if __name__ == '__main__':
    s = Solution()
    string = "eleetminicoworoep"
    print(s.findTheLongestSubstring(string))