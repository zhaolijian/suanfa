# 反转数位
# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
class Solution:
    def reverseBits(self, num: int) -> int:
        init = []
        temp = 0
        for i in range(32):
            if num & (1 << i):
                temp += 1
                if i == 31:
                    init.append(temp)
            else:
                init.append(temp)
                temp = 0
                if i == 31:
                    init.append(temp)
        length = len(init)
        if length == 1:
            return init[0]
        res = 0
        for i in range(1, length):
            res = max(res, init[i - 1] + init[i] + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    num = 2147483647
    print(s.reverseBits(num))