# ali 3.27
# 给定两个等长字符串，长度范围1e5，你可以选择第一个字符串的一个字符移动到字符串尾部，目的是让两个字符串相等，求最小的移动次数
# 问题可以转换为第一个字符串的子序列长度等于第二个字符串的前缀的最大匹配长度，最小移动次数是字符串长度-公共子序列长度
# 如果字符数量不匹配，则为false
import collections


class Solution:
    def solu(self, s1, s2):
        # 最大公共序列的长度
        max_len = 0
        # 如果字符数量不匹配，则为false
        s1_count = collections.Counter(s1)
        s2_count = collections.Counter(s2)
        for key, value in s1_count.items():
            if s1_count[key] != s2_count[key]:
                return -1
        # 求最大公共子序列长度
        for i in range(len(s1)):
            # 临时最大公共序列长度
            count = 0
            # 字符串2的当前遍历位置
            start = 0
            for j in range(i, len(s1)):
                # 如果遍历位置相等，则长度+1，继续往后遍历
                if s1[j] == s2[start]:
                    count += 1
                    start += 1
                # 如果不想等则break
                elif s1[j] != s2[start]:
                    break
                # 如果当前长度大于最大长度，则更新值
                if count > max_len:
                    max_len = count
        return len(s1) - max_len


if __name__ == '__main__':
    s = Solution()
    l = list(input().strip().split())
    s1, s2 = l[0], l[1]
    result = s.solu(s1, s2)
    print(result)

