# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 只有一个数字出现一次的话，直接对所有元素异或就可以了


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        temp = 0
        for ele in array:
            temp ^= ele
        i = 0
        while True:
            if (temp >> i) & 1:
                break
            i += 1
        number1, number2 = 0, 0
        for ele in array:
            if (ele >> i) & 1:
                number1 ^= ele
            else:
                number2 ^= ele
        return [number1, number2]