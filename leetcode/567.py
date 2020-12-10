# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 时间复杂度O(length2),空间复杂度O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_1, length_2 = len(s1), len(s2)
        if length_1 > length_2:
            return False
        d1, d2 = [0] * 26, [0] * 26
        for i in range(length_1):
            d1[ord(s1[i]) - ord('a')] += 1
            d2[ord(s2[i]) - ord('a')] += 1
        # 字符匹配相同的数量，如果count==26，则说明所有的字符串都匹配，返回true
        count = sum(d1[i] == d2[i] for i in range(26))
        if count == 26:
            return True
        for i in range(length_1, length_2):
            index = ord(s2[i]) - ord('a')
            d2[index] += 1
            if d2[index] == d1[index]:
                count += 1
            elif d2[index] == d1[index] + 1:
                count -= 1
            left = ord(s2[i - length_1]) - ord('a')
            d2[left] -= 1
            if d2[left] == d1[left]:
                count += 1
            elif d2[left] == d1[left] - 1:
                count -= 1
            if count == 26:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(s.checkInclusion(s1, s2))