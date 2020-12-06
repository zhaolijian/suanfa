# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = ""
        stack = []
        number = 0
        for ele in num:
            while number < k and stack and stack[-1] > ele:
                stack.pop()
                number += 1
            stack.append(ele)
        while number < k:
            stack.pop()
            number += 1
        while stack:
            res = stack.pop() + res
        # or: 从左到右扫描返回第一个为true的表达式,如果全为false,则返回最后一个表达式
        return res.lstrip("0") or "0"


if __name__ == '__main__':
    s = Solution()
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))