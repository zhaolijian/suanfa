class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def func(array, candidates, target):
            if target < 0:
                return
            elif target == 0:
                res.append(array)
            else:
                for i in range(len(candidates)):
                    func(array + [candidates[i]], candidates[i:], target - candidates[i])

        func([], candidates, target)
        return res