# 我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 的采样个数。
# 我们以 浮点数 数组的形式，分别返回样本的最小值、最大值、平均值、中位数和众数。其中，众数是保证唯一的。
# 我们先来回顾一下中位数的知识：
# 如果样本中的元素有序，并且元素数量为奇数时，中位数为最中间的那个元素；
# 如果样本中的元素有序，并且元素数量为偶数时，中位数为中间的两个元素的平均值


class Solution:
    def sampleStats(self, count):
        res = [float(0)] * 5
        # 最小值
        for i, ele in enumerate(count):
            if ele:
                res[0] = float(i)
                break
        # 最大值
        for i in range(255, -1, -1):
            if count[i]:
                res[1] = float(i)
                break
        # 平均值
        sum_val = 0
        number = 0
        # 众数值/次数
        common = -1
        common_number = 0
        for i in range(256):
            if count[i]:
                sum_val += count[i] * i
                number += count[i]
                if count[i] > common_number:
                    common_number = count[i]
                    common = i
        res[2] = sum_val / number
        res[4] = float(common)

        # 中位数
        mid = number / 2
        # 说明总数是奇数个
        if mid % 1:
            temp = 0
            for i in range(256):
                temp += count[i]
                if temp >= (number - 1) // 2:
                    res[3] = i
                    break
        # 说明总数是偶数个
        else:
            temp = 0
            number1, number2 = -1, -1
            for i in range(256):
                temp += count[i]
                if temp >= number // 2 and number1 == -1:
                    number1 = i
                if temp >= number // 2 + 1:
                    number2 = i
                    break
            res[3] = (number1 + number2) / 2
        return res