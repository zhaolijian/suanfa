# 判定字符是否唯一
# 位运算
class Solution:
    def isUnique(self, astr: str) -> bool:
        res = 0
        for i in range(len(astr)):
            temp = ord(astr[i]) - ord('a')
            if res & (1 << temp) != 0:
                return False
            else:
                res |= (1 << temp)
        return True


if __name__ == '__main__':
    s = Solution()
    astr = "leetcode"
    print(s.isUnique(astr))