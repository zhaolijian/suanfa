class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) < 3:
            return None
        nums.sort()
        res = float('inf')
        cha = float('inf')
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    temp = nums[l] + nums[r]
                    temp2 = nums[i] + temp - target
                    if temp2 == 0:
                        res = nums[i] + temp
                        return res
                    elif temp2 > 0:
                        if abs(temp2) < cha:
                            cha = abs(temp2)
                            res = nums[i] + temp
                        r -= 1
                    else:
                        if abs(temp2) < cha:
                            cha = abs(temp2)
                            res = nums[i] + temp
                        l += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = list(map(int, input().split()))
    target = int(input())
    print(s.threeSumClosest(nums, target))