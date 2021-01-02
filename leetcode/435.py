# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 注意:
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。


# 贪心算法
# 如果后一个区间的起点小于前一个区间的终点，那么为了移除最少区间数量，要移除终点比较大的
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0
        intervals.sort()
        # 区间尾部的位置
        end = intervals[0][1]
        # 需要移除的数量
        count= 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # 如果重叠了,必须移除一个,count要+1,然后更新尾部的位置,取尾部比较小的
                end = min(end, intervals[i][1])
                count += 1
            else:
                # 如果没有重叠,就不需要移除,只需要更新尾部位置即可
                end = intervals[i][1]
        return count