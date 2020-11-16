# 给你两个数组，arr1 和 arr2，
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。


# 方法1
from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1, arr2):
        set_array = set(arr2)
        d = defaultdict(int)
        res = []
        temp = []
        for ele in arr1:
            if ele in set_array:
                d[ele] += 1
            else:
                temp.append(ele)
        for ele in arr2:
            if ele in d:
                res += [ele] * d[ele]
        temp.sort()
        return res + temp



# 方法2
from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_value = max(arr1)
        array = [0] * (max_value + 1)
        res = []
        for ele in arr1:
            array[ele] += 1
        for ele in arr2:
            if array[ele]:
                res += [ele] * array[ele]
                array[ele] = 0
        for i, ele in enumerate(array):
            if ele:
                res += [i] * ele
        return res