# 编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。
# 待填充的图像用二维数组 image 表示，元素为初始颜色值。初始坐标点的横坐标为 sr 纵坐标为 sc。需要填充的新颜色为 newColor 。
# 「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。
# 请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        def func(sr, sc):
            nonlocal h, w
            init[sr][sc] = True
            temp = image[sr][sc]
            image[sr][sc] = newColor
            if sr > 0 and not init[sr - 1][sc] and temp == image[sr - 1][sc]:
                func(sr - 1, sc)
            if sr < h - 1 and not init[sr + 1][sc] and temp == image[sr + 1][sc]:
                func(sr + 1, sc)
            if sc > 0 and not init[sr][sc - 1] and temp == image[sr][sc - 1]:
                func(sr, sc - 1)
            if sc < w - 1 and not init[sr][sc + 1] and temp == image[sr][sc + 1]:
                func(sr, sc + 1)

        h, w = len(image), len(image[0])
        # 是否访问数组
        init = [[False for i in range(w)] for j in range(h)]
        func(sr, sc)
        return image


if __name__ == '__main__':
    s = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(s.floodFill(image, sr, sc, newColor))