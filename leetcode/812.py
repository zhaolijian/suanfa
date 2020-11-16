class Solution:
    def largestTriangleArea(self, points) -> float:
        max_area = 0
        length = len(points)
        for i in range(length-2):
            point1_x = float(points[i][0])
            point1_y = float(points[i][1])
            for j in range(i+1, length-1):
                point2_x = float(points[j][0])
                point2_y = float(points[j][1])
                for m in range(j+1, length):
                    point3_x = float(points[m][0])
                    point3_y = float(points[m][1])
                    area = abs(point1_x * point2_y + point2_x * point3_y + point3_x * point1_y - point1_x * point3_y - point2_x * point1_y - point3_x * point2_y)/2
                    if area > max_area:
                        max_area = area
        return max_area


if __name__ == '__main__':
    s = Solution()
    area = s.largestTriangleArea([[4,6],[6,5],[3,1]])
    print(area)