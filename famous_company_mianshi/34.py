# 给定一个double类型的数组arr，其中的元素可正可负可0，返回子数组累乘的最大乘积。
# 例如arr=[-2.5，4，0，3，0.5，8，-1]，子数组[3，0.5，8]累乘可以获得最大的乘积12，所以返回12。

class Solution:
    def maxProduct(self , arr ):
        # write code here
        if not arr:
            return None
        length = len(arr)
        min_array = [1] * length
        min_array[0] = arr[0]
        max_array = [1] * length
        max_array[0] = arr[0]
        for i in range(1, length):
            if arr[i] > 0:
                min_array[i] = arr[i] if min_array[i - 1] > 1 else min_array[i - 1] * arr[i]
                max_array[i] = arr[i] if max_array[i - 1] < 1 else max_array[i - 1] * arr[i]
            else:
                min_array[i] = max_array[i - 1] * arr[i] if max_array[i - 1] > 1 else arr[i]
                max_array[i] = min_array[i - 1] * arr[i] if min_array[i - 1] < 1 else arr[i]
        return max(max_array)


if __name__ == '__main__':
    s = Solution()
    arr = [0.1, 0.0, 3.0, -2.0, 0.9, -1.3, 5.0, -4.4]
    print(s.maxProduct(arr))