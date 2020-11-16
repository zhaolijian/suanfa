import collections
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if abs(len1 - len2) >= 2:
            return False
        if len1 == len2:
            diff = 0
            for i in range(len1):
                if first[i] != second[i]:
                    diff += 1
            return True if diff <= 1 else False
        else:
            diff = 0
            if len1 > len2:
                first, second = second, first
            min_len, max_len = min(len1, len2), max(len1, len2)
            i, j = 0, 0
            while i < min_len and j < max_len:
                if first[i] == second[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    diff += 1
                    if diff >= 2:
                        return False
            return True


if __name__ == '__main__':
    s = Solution()
    first, second = "pale", "ple"
    print(s.oneEditAway(first, second))