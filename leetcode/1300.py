# 方法1 二叉查找
import bisect
class Solution:
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        length = len(arr)
        # 累计和
        array = [0]
        for i in range(length):
            array.append(array[-1] + arr[i])
        res = -1
        cha = float('inf')
        min_value, max_vlaue = 0 if arr[0] * length > target else arr[0], arr[-1]
        while min_value < max_vlaue:
            middle_value = (min_value + max_vlaue) // 2
            # 查找middle_value如果插入到arr中的话，应该插入的位置，有相同的值插入到左边
            index = bisect.bisect_left(arr, middle_value)
            temp = array[index] + (length - index) * middle_value
            # 如果不使用bisect.bisect_left
            # temp = 0
            # for i in range(length):
            #     if arr[i] < middle_value:
            #         temp += arr[i]
            #     else:
            #         temp += middle_value
            temp_cha = abs(temp - target)
            if temp_cha < cha:
                cha = temp_cha
                res = middle_value
            elif temp_cha == cha:
                res = min(res, middle_value)
            if temp == target:
                return middle_value
            elif temp > target:
                max_vlaue = middle_value
            else:
                min_value = middle_value + 1
        temp = 0
        for i in range(length):
            if arr[i] < min_value:
                temp += arr[i]
            else:
                temp += min_value
        temp_cha = abs(temp - target)
        if temp_cha < cha:
            res = min_value
        elif temp_cha == cha:
            res = min(res, min_value)
        return res
    

if __name__ == '__main__':
    s = Solution()
    arr = [4,9,3]
    target = 10
    print(s.findBestValue(arr, target))