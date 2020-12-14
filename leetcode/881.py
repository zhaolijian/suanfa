# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。


class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        res = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if left == right:
                res += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                res += 1
            else:
                right -= 1
                res += 1
        return res