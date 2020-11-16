class Solution:
    def spiralOrder(self, matrix):
        height = len(matrix)
        if not height:
            return []
        width = len(matrix[0])
        if not width:
            return []
        l, r, t, b = 0, width - 1, 0, height - 1
        res = []
        while l <= r and t <= b:
            res += matrix[t][l: r + 1]
            t += 1
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if t > b or l > r:
                break
            else:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[7],[9],[6]]
    # print(matrix[: 3][2])
    print(s.spiralOrder(matrix))