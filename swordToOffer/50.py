class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        init = [0 for i in range(len(numbers))]
        for ele in numbers:
            if init[ele] > 0:
                duplication[0] = ele
                return True
            init[ele] += 1
        return False


# 该方法占用的内存小，对遍历的值不断进行扩展
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        init = []
        for ele in numbers:
            if len(init) <= ele:
                init += [0] * (ele - len(init) + 1)
            if init[ele] > 0:
                duplication[0] = ele
                return True
            else:
                init[ele] += 1
        return False