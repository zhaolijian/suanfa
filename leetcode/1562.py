# 给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。
# 在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。
# 给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。
# 一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。
# 返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。


# 方法1 双百
# 每操作一次，新增的 1 可能会有如下三种情况：
# 左右都是 0。此时该位置作为新增段独立存在。
# 仅有左边或者右边。此时该位置会将某个旧段的长度加 1。
# 左右都是 1。此时该位置会将两个旧段合并成一个新段。
class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        # 前后各加一个0
        # 全为1的子串，头指向尾位置，尾指向头位置
        link = [0] * (len(arr) + 2)
        # 段长为m的个数
        cnt = 0
        res = -1
        for i in range(len(arr)):
            x = arr[i]
            l = link[x - 1] if link[x - 1] else x
            r = link[x + 1] if link[x + 1] else x
            if x - l == m:
                cnt -= 1
            if r - x == m:
                cnt -= 1
            if r - l + 1 == m:
                cnt += 1
            if cnt > 0:
                res = i + 1
            link[l] = r
            link[r] = l
        return res


# 方法2
class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n = len(arr)
        nums = []
        dp = [0]*n
        cnt = 0
        ans = -1
        for i,a in enumerate(arr):
            cur = a-1
            start = end = cur
            if cur-1>=0:
                dp[cur] += dp[cur-1]
                start = cur-dp[cur-1]
            if cur+1<n:
                dp[cur] += dp[cur+1]
                end = cur+dp[cur+1]
            dp[cur]+=1
            if cur-1>=0:
                dp[cur-dp[cur-1]] = dp[cur]
            if cur+1<n:
                dp[cur+dp[cur+1]] = dp[cur]
            if dp[cur]==m:
                nums.append([start, end])
            for start, end in nums:
                if dp[start]==m and dp[end]==m:
                    ans = i+1
        return ans


# 方法2
import collections
class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n = len(arr)
        # 长度为某个值的数量
        lenToCnt = collections.defaultdict(int)
        # 起始和终止位置的长度
        iToLen = {}
        res = -1
        for index, x in enumerate(arr):
            # 转成以0为起点的下标
            i = x - 1
            # 原来的左侧和右侧的连续1的长度
            left = 0
            right = 0
            # 新的连续1的起点和终点下标, 初始化为当前下标
            start = i
            end = i
            if i - 1 >= 0 and i - 1 in iToLen:
                # 更新左侧长度和起点下标
                left = iToLen[i - 1]
                start -= left
            if i + 1 < n and i + 1 in iToLen:
                # 更新右侧长度和终点下标
                right = iToLen[i + 1]
                end += right
            newlen = left + right + 1
            # 更新iToLen字典, 只需要更新两个边界即可
            iToLen[start] = newlen
            iToLen[end] = newlen
            # 更新lenToCnt字典, 减去旧长度的值, 加上新长度的值
            lenToCnt[left] -= left
            lenToCnt[right] -= right
            lenToCnt[newlen] += newlen
            if lenToCnt[m] > 0:
                # 如果仍有连续1长度为m的部分, 更新最终结果为当前arr下标+1
                res = index + 1
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [3,5,1,2,4]
    m = 1
    print(s.findLatestStep(arr, m))