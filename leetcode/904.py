# 在一排树中，第 i 棵树产生 tree[i] 型的水果。
# 你可以从你选择的任何树开始，然后重复执行以下步骤：
# 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
# 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
# 请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
# 你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
# 用这个程序你能收集的水果树的最大总量是多少？


from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counter = Counter()
        res = i = 0
        for j, ele in enumerate(tree):
            counter[ele] += 1
            while len(counter) >= 3:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    counter.pop(tree[i])
                i += 1
            res = max(res, j - i + 1)
        return res


from collections import defaultdict
class Solution:
    def totalFruit(self, tree) -> int:
        if len(tree) < 2:
            return 1
        res = 0
        left, right = 0, 1
        d = defaultdict(int)
        # 树的品种及对应的数量
        d[tree[0]] = 1
        while right < len(tree):
            if tree[right] in d or len(d.keys()) < 2:
                d[tree[right]] += 1
                res = max(res, right - left + 1)
                right += 1
            else:
                # 要保留的树的品种
                type = tree[right - 1]
                while left < right:
                    if tree[left] != type:
                        d[tree[left]] -= 1
                        if d[tree[left]] == 0:
                            d.pop(tree[left])
                            left += 1
                            break
                    else:
                        d[type] -= 1
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    tree = [1,0,1,4,1,4,1,2,3]
    print(s.totalFruit(tree))