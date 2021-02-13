# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            last_array = [1,1]
            for i in range(2, rowIndex + 1):
                array = [1]
                for j in range(1, i):
                    array.append(last_array[j - 1] + last_array[j])
                array.append(1)
                last_array = array
            return array



if __name__ == '__main__':
    s = Solution()
    rowIndex = 3
    print(s.getRow(rowIndex))