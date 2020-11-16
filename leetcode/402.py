# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if k >= length:
            return "0"
        res = ""
        stack = []
        number = 0
        flag = False
        for ele in num:
            if not flag:
                while stack and stack[-1] > ele:
                    stack.pop()
                    number += 1
                    if number >= k:
                        flag = True
                        break
            stack.append(ele)
        while number < k:
            stack.pop()
            number += 1
        while stack:
            res = stack.pop() + res
        # 去掉前缀为0
        index = -1
        for i, ele in enumerate(res):
            if ele == '0':
                index = i
            else:
                break
        return res[index + 1:]


if __name__ == '__main__':
    s = Solution()
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))