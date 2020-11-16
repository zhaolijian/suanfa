# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         length = len(array)
#         res = [0, 0]
#         if length == 2:
#             res[0] = array[0]
#             res[1] = array[1]
#             return res
#         bitResult = 0
#         # 所有数进行异或操作
#         for i in range(length):
#             bitResult ^= array[i]
#         index = self.findFirst(bitResult)
#         for i in range(length):
#             if self.isBit(array[i], index):
#                 res[0] ^= array[i]
#             else:
#                 res[1] ^= array[i]
#         return res
#
#     # 找到第一个二进制位为1的位
#     def findFirst(self, bitResult):
#         index = 0
#         while bitResult & 1 == 0:
#             bitResult >>= 1
#             index += 1
#         return index
#
#     def isBit(self, target, index):
#         return ((target >> index) & 1) == 1


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return
        if len(array) == 2:
            return [array[0], array[1]]
        temp = 0
        res = [0, 0]
        for ele in array:
            temp ^= ele
        index = 0
        while index < len(array):
            if temp & 1 == 0:
                temp >>= 1
                index += 1
            else:
                break
        for ele in array:
            if (ele >> index) & 1 == 1:
                res[0] ^= ele
            else:
                res[1] ^= ele
        return res


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().split()))
    print(s.FindNumsAppearOnce(l))
