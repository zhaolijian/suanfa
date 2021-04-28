# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。


class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        max_weight = max(weights)
        length = len(weights)
        # 平均每艘船运的货物数量
        temp = length // D if length % D == 0 else length // D + 1
        sorted_weights = sorted(weights)
        # 最大运载能力（最大就是最重的temp个货物）
        max_val = sum(sorted_weights[length - temp:])
        # 最小运载能力
        min_val = max_weight
        # 二分法
        while min_val < max_val:
            # 运载能力
            mid_val = (min_val + max_val) // 2
            temp = 0
            number = 1
            for weight in weights:
                temp += weight
                if temp > mid_val:
                    number += 1
                    temp = weight
            if number > D:
                min_val = mid_val + 1
            else:
                max_val = mid_val
        return min_val