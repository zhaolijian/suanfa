# 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
# 返回这两个区间列表的交集。
#（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。
# 例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）


class Solution:
    def intervalIntersection(self, A, B):
        len_A, len_B = len(A), len(B)
        if len_A == 0 or len_B == 0:
            return []
        res = []
        i, j = 0, 0
        while i < len_A and j < len_B:
            A_left, A_right = A[i]
            B_left, B_right = B[j]
            if A_right < B_left:
                i += 1
            elif B_right < A_left:
                j += 1
            else:
                res.append([max(A_left, B_left), min(A_right, B_right)])
                if A_right > B_right:
                    j += 1
                else:
                    i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print(s.intervalIntersection(A, B))