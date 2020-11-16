# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。


class Solution:
    def commonChars(self, A):
        init = [float('inf')] * 26
        for i in range(len(A)):
            temp = [0] * 26
            for ele in A[i]:
                temp[ord(ele) - 97] += 1
            for i in range(26):
                init[i] = min(init[i], temp[i])
        res = []
        for i in range(26):
            if init[i]:
                res += chr(i + 97) * init[i]
        return res




from collections import Counter
class Solution:
    def commonChars(self, A):
        init = [0] * 26
        first = Counter(A[0])
        for key, val in first.items():
            init[ord(key) - 97] += val
        for i in range(1, len(A)):
            temp = [0] * 26
            for ele in A[i]:
                temp[ord(ele) - 97] += 1
            for i in range(26):
                init[i] = min(init[i], temp[i])
        res = []
        for i in range(26):
            if init[i]:
                res += chr(i + 97) * init[i]
        return res


if __name__ == '__main__':
    s = Solution()
    A = ["bella","label","roller"]
    print(s.commonChars(A))