# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
# 注意:
# 字符串长度 和 k 不会超过 104。

# 使用双指针维护这些区间，每次右指针右移，如果区间仍然满足条件，那么左指针不移动，否则左指针至多右移一格，保证区间长度不减小
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left, right = 0, 0
        max_char_length = 0
        while right < len(s):
            d[s[right]] += 1
            max_char_length = max(max_char_length, d[s[right]])
            if right - left + 1 - max_char_length > k:
                d[s[left]] -= 1
                left += 1
            right += 1
        return right - left
    

if __name__ == '__main__':
    s = Solution()
    ss = "AABA"
    k = 0
    print(s.characterReplacement(ss, k))