# 编写一个程序，通过填充空格来解决数独问题。
# 数独的解法需 遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


# dfs
class Solution:
    def solveSudoku(self, board) -> None:
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        zones = [[set() for i in range(3)] for j in range(3)]
        array = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    array.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    zones[i//3][j//3].add(board[i][j])
        def dfs(number):
            if number == len(array):
                return True
            i, j = array[number]
            rest = nums - rows[i] - cols[j] - zones[i // 3][j // 3]
            if not rest:
                return False
            for ele in rest:
                board[i][j] = ele
                rows[i].add(ele)
                cols[j].add(ele)
                zones[i // 3][j // 3].add(ele)
                if dfs(number + 1):
                    return True
                rows[i].remove(ele)
                cols[j].remove(ele)
                zones[i // 3][j // 3].remove(ele)
        dfs(0)