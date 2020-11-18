# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
# 说明: 
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。


# 方法1,画图的方式看出在那个位置欠的油最多，如果跑完一圈，油量还是小于0，则返回-1，否则欠油最多的位置的下一个位置即为所求。时间复杂度O(n),空间复杂度O(1)
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        length = len(gas)
        # 车跑到下一个节点剩余的油量
        cur = 0
        min_val = 0
        index = 0
        for i in range(length):
            cur += gas[i] - cost[i]
            if cur < min_val:
                min_val = cur
                index = i + 1
        if cur < 0:
            return -1
        return index % length


# 方法2
# 如果x索引第一个无法到达的索引点是y,那么从x,y中间的任意节点z也都无法到达y.
# 因为从x到z剩余的油量肯定是大于等于0的,对从z出发是有助益的,这样都无法到达y,那么从z到y肯定也无法到达.所以从下一个索引点开始遍历
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        # 走完一圈最终剩下的油量
        result = 0
        length = len(gas)
        cur = 0
        index = 0
        for i in range(length):
            result += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                index = i + 1
        return -1 if result < 0 else index


# 方法3，最笨的方法，遍历所有点，找出所有情况
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        length = len(gas)
        gas += gas
        cost += cost
        # 起始加油站
        for i in range(length):
            cur = gas[i]
            for j in range(i, i + length):
                cur -= cost[j]
                if cur < 0:
                    break
                if (j + 1) % length == i:
                    return i
                cur += gas[j + 1]
        return -1


if __name__ == '__main__':
    s = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(s.canCompleteCircuit(gas, cost))