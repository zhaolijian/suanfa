# 方法1 一次遍历，双指针
class Solution:
    def subSort(self, array):
        length = len(array)
        if length == 0 or length == 1:
            return [-1, -1]
        start, end = -1, -1
        max_val, min_val = float('-inf'), float('inf')
        for i in range(length):
            # 从左往右遍历，如果遍历值小于从左往右遍历数中的最大值，则返回区间的右侧值赋值为当前遍历点
            if array[i] >= max_val:
                max_val = array[i]
            else:
                end = i

            # 从右往左遍历，如果遍历值大于从右往左遍历数中的最小值，则返回区间的左侧值赋值为length - 1 - i
            if array[length - 1 - i] <= min_val:
                min_val = array[length - 1 - i]
            else:
                start = length - 1 - i
        return [start, end]


# 方法2 栈，两次遍历
# class Solution:
#     def subSort(self, array):
#         length = len(array)
#         if length <= 1:
#             return [-1, -1]
#         start, end = float('inf'), float('-inf')
#         stack1, stack2 = [], []
#         for i in range(length):
#             if not stack1 or array[i] >= array[stack1[-1]]:
#                 stack1.append(i)
#             else:
#                 while stack1:
#                     if array[i] < array[stack1[-1]]:
#                         start = min(start, stack1.pop())
#                     else:
#                         stack1.append(i)
#                         break
#         for i in range(length - 1, -1, -1):
#             if not stack2 or array[i] <= array[stack2[-1]]:
#                 stack2.append(i)
#             else:
#                 while stack2:
#                     if array[i] > array[stack2[-1]]:
#                         end = max(end, stack2.pop())
#                     else:
#                         stack2.append(i)
#                         break
#         return [start, end] if start != float('inf') and end != float('-inf') else [-1, -1]


if __name__ == '__main__':
    s = Solution()
    array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    print(s.subSort(array))