class Solution:
    def find132pattern(self, nums) -> bool:
        length = len(nums)
        if length < 3:
            return False
        else:
            # 开始位置到当前位置的最小值数组
            min_array = [nums[0]]
            stack = []
            for i in range(1, length):
                min_array.append(min(min_array[i - 1], nums[i]))
            for j in range(length - 1, -1, -1):
                # 当前遍历值必须大于开始到当前位置最小值
                if nums[j] > min_array[j]:
                    while stack and stack[-1] <= min_array[j]:
                        stack.pop()
                    if stack and nums[j] > stack[-1]:
                        return True
                    stack.append(nums[j])
            return False
        

if __name__ == '__main__':
    s = Solution()
    nums = [3,1,4,2]
    print(s.find132pattern(nums))