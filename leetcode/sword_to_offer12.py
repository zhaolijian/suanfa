# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
# 如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
# 例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
class Solution:
    def exist(self, board, word: str) -> bool:
        def bfs(i, j, word):
            nonlocal h, w
            if not 0 <= i <= h - 1 or not 0 <= j <= w - 1:
                return False
            if not word or (len(word) == 1 and board[i][j] == word[0]):
                return True
            if board[i][j] != word[0]:
                return False
            temp, board[i][j] = board[i][j], '/'
            res = bfs(i + 1, j, word[1:]) or bfs(i - 1, j, word[1:]) or bfs(i, j + 1, word[1:]) or bfs(i, j - 1, word[1:])
            board[i][j] = temp
            return res

        if not word:
            return False
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if bfs(i, j, word):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(s.exist(board, word))