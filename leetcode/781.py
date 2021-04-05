# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
# 返回森林中兔子的最少数量。
from collections import Counter
class Solution:
    def numRabbits(self, answers) -> int:
        if not answers:
            return 0
        d = Counter(answers)
        res = 0
        for key in d.keys():
            if key == 0:
                res += d[key]
            elif d[key] <= key + 1:
                res += key + 1
            else:
                number = d[key] // (key + 1)
                temp = d[key] % (key + 1)
                res += (number + 1) * (key + 1) if temp else number * (key + 1)
        return res