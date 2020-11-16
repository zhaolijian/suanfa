# 给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
# 注意：
# 三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
# 解集中不能包含重复的三元组。
class Solution:
    def threeSum(self , num):
        length = len(num)
        if length < 3:
            return []
        num.sort()
        set_array = set()
        for i in range(length - 2):
            if num[i] > 0:
                break
            target = -num[i]
            l, r = i + 1, length - 1
            while l < r:
                if num[l] + num[r] == target:
                    set_array.add((num[i], num[l], num[r]))
                    l += 1
                    r -= 1
                elif num[l] + num[r] > target:
                    r -= 1
                else:
                    l += 1
        return sorted(list(set_array))


if __name__ == '__main__':
    s = Solution()
    num = [-2,0,1,1,2]
    print(s.threeSum(num))