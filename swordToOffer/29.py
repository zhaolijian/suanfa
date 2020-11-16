# -*- coding:utf-8 -*-
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
# 利用冒泡排序的思想


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 1 and k == 1:
            return tinput
        elif tinput == [] or k > len(tinput):
            return []
        # 比较的次数，每一次比较确定一个值
        for i in range(k):
            for j in range(len(tinput)-i-1, 0, -1):
                if tinput[j] < tinput[j-1]:
                    tinput[j], tinput[j-1] = tinput[j-1], tinput[j]
        return quick_sort(tinput[:k])


def quick_sort(l):
    if len(l) <= 1:
        return l
    temp = l[0]
    # 小于temp的部分
    left = quick_sort([x for x in l[1:] if x < temp])
    # 大于temp的部分
    right = quick_sort([x for x in l[1:] if x >= temp])
    return left + [temp] + right


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().strip().split()))
    k = int(input())
    print(s.GetLeastNumbers_Solution(l, k))
