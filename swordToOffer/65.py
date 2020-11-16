class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix:
            return False
        if not path:
            return True
        init = [list(matrix[i * cols: i * cols + cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.find(init, i, j, path):
                    return True
        return False

    def find(self, matirx, i, j, path):
        if matirx[i][j] == path[0]:
            if not path[1:]:
                return True
            matirx[i][j] = ''
            if i > 0 and self.find(matirx, i - 1, j, path[1:]):
                return True
            if i < len(matirx) - 1 and self.find(matirx, i + 1, j, path[1:]):
                return True
            if j > 0 and self.find(matirx, i, j - 1, path[1:]):
                return True
            if j < len(matirx[0]) - 1 and self.find(matirx, i, j + 1, path[1:]):
                return True
            matirx[i][j] = path[0]
            return False
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    l = "ABCESFCSADEE"
    ss = 'ABCCED'
    print(s.hasPath(l, 3, 4, ss))
    ll = [1, 2]
    if not ll[2:]:
        print(False)
    print(ll[2:])


