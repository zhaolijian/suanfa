# 你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
# 视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，
# 例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。


# 动态规划
class Solution:
    def videoStitching(self, clips, T: int) -> int:
        # 对于每一个值表示[0, i)的最少段数
        dp = [0] + [float('inf')] * T
        for i in range(1, T + 1):
            for first, second in clips:
                if first < i <= second:
                    dp[i] = min(dp[i], dp[first] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]


# 贪心算法（不太懂）

# 每次我们枚举到一个新位置，我们都用maxn[i]来更新last。如果更新后last == i，那么说明下一个位置无法被覆盖，我们无法完成目标。
# 同时我们还需要记录上一个被使用的子区间的结束位置为pre，每次我们越过一个被使用的子区间，就说明我们要启用一个新子区间，这个新子区间的结束位置即为当前的last。
# 也就是说，每次我们遇到i == pre，则说明我们用完了一个被使用的子区间。这种情况下我们让答案加1，并更新pre即可

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 记录每一个位置能够到达的最远位置
        maxn = [0] * T
        # last: 新子区间的结束位置
        # pre: 上一个被使用的子区间的结束位置
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret
