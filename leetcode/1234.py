# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
# 请返回待替换子串的最小可能长度。
# 如果原字符串自身就是一个平衡字符串，则返回 0。


from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        c = Counter(s)
        # 让窗口外的字符小于等于平均值
        length = len(s)
        # 窗口外字符的个数大于平均值的个数
        number = 0
        for key in c:
            if c[key] > length // 4:
                number += 1
        if number == 0:
            return 0
        res = float('inf')
        left, right = 0, 0
        while right < length:
            c[s[right]] -= 1
            if c[s[right]] == length // 4:
                number -= 1
            if number == 0:
                while left <= right:
                    c[s[left]] += 1
                    if c[s[left]] > length // 4:
                        res = min(res, right - left + 1)
                        c[s[left]] -= 1
                        break
                    left += 1
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    ss = "WQWRQQQW"
    print(s.balancedString(ss))