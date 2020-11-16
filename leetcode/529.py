class Solution:
    def updateBoard(self, board, click):
        def dfs(i, j):
            if not (0 <= i < height and 0 <= j < width and board[i][j] == 'E'):
                return
            d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            # 记录炸弹数
            temp = 0
            for x, y in d:
                if 0 <= i + x < height and 0 <= j + y < width and board[i + x][j + y] == 'M':
                    temp += 1
            if temp > 0:
                board[i][j] = str(temp)
            else:
                board[i][j] = 'B'
                for x, y in d:
                    dfs(i + x, j + y)

        if not board or not board[0]:
            return board
        height, width = len(board), len(board[0])
        if not 0 <= click[0] < height or not 0 <= click[1] < width:
            return board
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        dfs(click[0], click[1])
        return board


if __name__ == '__main__':
    s = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    print(s.updateBoard(board, click))