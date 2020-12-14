# 有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
# 现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
# 每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。
# 举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。
# 我们能得到的最大收益是多少？


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = []
        for i, ele in enumerate(difficulty):
            jobs.append((ele, profit[i]))
        jobs.sort()
        worker.sort()
        j = 0
        cur_profix = 0
        res = 0
        for ele in worker:
            while j < len(difficulty) and ele >= jobs[j][0]:
                cur_profix = max(cur_profix, jobs[j][1])
                j += 1
            res += cur_profix
        return res


if __name__ == '__main__':
    s = Solution()
    difficulty = [68,35,52,47,86]
    profit = [67,17,1,81,3]
    worker = [92,10,85,84,82]
    print(s.maxProfitAssignment(difficulty, profit, worker))