# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
# 接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。
# 将所有有记录的像素点的颜色值改为新的颜色值。最后返回经过上色渲染后的图像。


# 方法1 dfs
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        height, width = len(image), len(image[0])
        init = image[sr][sc]
        def dfs(i, j):
            if not (0 <= i < height and 0 <= j < width) or image[i][j] == newColor:
                return
            if image[i][j] == init:
                image[i][j] = newColor
                d = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for x, y in d:
                    dfs(i + x, j + y)
        dfs(sr, sc)
        return image


# 方法2 bfs
from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        height, width = len(image), len(image[0])
        init_color = image[sr][sc]
        if init_color == newColor:
            return image
        queue = deque([(sr, sc)])
        while queue:
            i, j = queue.popleft()
            image[i][j] = newColor
            d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in d:
                if 0 <= i + x < height and 0 <= j + y < width and image[i + x][j + y] == init_color:
                    queue.append((i + x, j + y))
        return image