from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N, paths):
        res = [1] * N
        d = defaultdict(list)
        for first, second in paths:
            if first < second:
                d[second - 1].append(first - 1)
            else:
                d[first - 1].append(second - 1)
        d = sorted(d.items())
        for key, array in d:
            # ({1, 2, 3, 4} - {res[ele] for ele in array})是一个字典，对于字典，pop函数返回的是第一个元素
            res[key] = ({1, 2, 3, 4} - {res[ele] for ele in array}).pop()
        return res


if __name__ == '__main__':
    s = Solution()
    N = 5
    paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
    print(s.gardenNoAdj(N, paths))