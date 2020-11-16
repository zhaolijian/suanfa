# 特殊串：0和1的数量相等，前缀符1的数量大于等于0的数量
# 两个特殊字串交换，要最大


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S:
            return ''
        length = len(S)
        pre = 0
        count = 0
        sub_string = []
        temp_string = S
        for i in range(pre, length):
            if S[i] == '1':
                count += 1
            elif S[i] == '0':
                count -= 1
            if count == 0:
                sub_string.append('1' + self.makeLargestSpecial(temp_string[pre+1:i]) + '0')
                pre = i + 1
        return ''.join(sorted(sub_string, reverse=True))


if __name__ == '__main__':
    s = Solution()
    print(s.makeLargestSpecial('11011000'))
