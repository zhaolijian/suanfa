# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
class Solution:
    def combinationSum2(self, candidates, target: int):
        if target == 0 or len(candidates) == 0:
            return []
        result = []

        def helper(tar, idx, cur):
            if tar == 0:  # 终止条件
                result.append(cur[:])
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # 下面调用helper时，第二个参数的位置是i+1，一定是从当前一位的下一位开始找(开始的时候写成了idx，一直无法减枝)
                helper(tar - candidates[i], i + 1, cur + [candidates[i]])

        candidates.sort()
        helper(target, 0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))