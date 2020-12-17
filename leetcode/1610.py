# 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。
# 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示，
# 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。
# 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。
# 同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。
# 返回你能看到的点的最大数目。


from math import atan2, pi
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        res = 0
        angle_array = []
        # 将points数组中点与location所成的角度转换为pi的形式
        for x, y in points:
            if x == location[0] and y == location[1]:
                res += 1
                continue
            temp = atan2(y - location[1], x - location[0]) + pi
            angle_array.append(temp)
        angle_array.sort()
        # 数组 加上 每个元素值+2*pi的数组是为了解决0度和360度是一个闭环的问题
        angle_array += [a + 2 * pi for a in angle_array]
        left, right = 0, 0
        angle = angle / 180 * pi
        cur = 0
        while right < len(angle_array):
            if angle_array[right] - angle_array[left] <= angle:
                cur = max(cur, right - left + 1)
                right += 1
            else:
                while angle_array[right] - angle_array[left] > angle:
                    left += 1
        return res + cur


if __name__ == '__main__':
    s = Solution()
    points = [[0,0],[0,2]]
    angle = 90
    location = [1,1]
    print(s.visiblePoints(points, angle, location))