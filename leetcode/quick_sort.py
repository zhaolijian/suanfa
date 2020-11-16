import random
# class Solution:
#     def quick_sort(self, array, left, right):
#         if left >= right:
#             return array
#         low = left
#         high = right
#         key = array[low]
#         while left < right:
#             while left < right and array[right] >= key:
#                 right -= 1
#             array[left] = array[right]
#             while left < right and array[left] <= key:
#                 left += 1
#             array[right] = array[left]
#         array[right] = key
#         self.quick_sort(array, low, left - 1)
#         self.quick_sort(array, left + 1, high)
#         return array
class Solution:
    def quick_sort(self, array, left, right):
        if left >= right:
            return array

        l, r = left, right
        key = array[left]
        while l < r:
            while l < r and array[r] >= key:
                r -= 1
            array[l] = array[r]
            while l < r and array[l] <= key:
                l += 1
            array[r] = array[l]
        array[r] = key
        self.quick_sort(array, left, l - 1)
        self.quick_sort(array, l + 1, right)
        return array


if __name__ == '__main__':
    s = Solution()
    array = [random.randint(1, 30) for i in range(10)]
    print(s.quick_sort(array, left=0, right=9))