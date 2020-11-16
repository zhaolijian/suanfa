# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 思路就是将intervals数组中与newInterval有交集的区间合并成一个区间
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # 是否有交集
        intersect = False
        left, right = newInterval[0], newInterval[1]
        for l, r in intervals:
            if r < left:
                res.append([l, r])
            elif l > right:
                # 当前遍历区间与[left,right]无交集,且当前遍历区间在[left,right]右侧
                if not intersect:
                    res.append([left, right])
                    intersect = True
                res.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        # 说明[left,right]区间已经与最右侧区间融合了
        if not intersect:
            res.append([left, right])
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval[0], newInterval[1]
        index = -1
        for i, [l, r] in enumerate(intervals):
            if l <= left <= r or l <= right <= r:
                left = min(left, l)
                right = max(right, r)
            elif right < l:
                index = i
                break
        for i, [l, r] in enumerate(intervals):
            if r < left:
                res.append([l, r])
            else:
                break
        res.append([left, right])
        if index != -1:
            for i in range(index, len(intervals)):
                res.append(intervals[i])
        return res



if __name__ == '__main__':
    s = Solution()
    intervals = [[1,5]]
    newInterval = [5,7]
    print(s.insert(intervals, newInterval))