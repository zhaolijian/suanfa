class Solution:
    def readBinaryWatch(self, num: int):
        result = []
        for i in range(12):
            for j in range(60):
                if self.num_one(i) + self.num_one(j) == num:
                    if j < 10:
                        result.append(str(i) + ':0' + str(j))
                    else:
                        result.append(str(i) + ':' + str(j))
        return result

        # 获得1的个数

    def num_one(self, number: int):
        res = 0
        while number != 0:
            number = number & (number - 1)
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(0))
