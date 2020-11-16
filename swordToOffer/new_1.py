# -*- coding:utf-8 -*-
# n个整数的无序数组，找到每个元素后面比它大的第一个数，要求时间复杂度为O(N)


class Solution:
    def ss(self, l):
        len_l = len(l)
        if len_l == 0:
            return l
        # 栈
        array = []
        # 返回的数组
        res = l
        i = 0
        while i < len_l:
            # 如果当前遍历值比栈顶值小或者栈为空，则将当前遍历值放入栈中
            if len(array) == 0 or l[i] <= l[array[-1]]:
                array.append(i)
                i += 1
            # 如果当前遍历值比栈顶元素大，则递归删除比当前遍历值小的元素，并将遍历值放入栈中及将遍历值放入返回数组中适当位置
            else:
                res[array[-1]] = l[i]
                array.pop()
        # 栈中还不为空，说明没有值比它们大，则将
        while len(array) != 0:
            res[array[-1]] = 2147483647
            array.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    input_values = list(map(int, input().strip().split()))
    result = s.ss(input_values)
    print(result)

