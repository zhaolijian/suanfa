# 方法1 飞快
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        length_min = shorter*k
        length_max = longer*k
        dist = longer-shorter
        return list(range(length_min,length_max+1,dist))


# 方法2
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        res = []
        base = shorter * k
        # 差值
        cha = longer - shorter
        for i in range(k + 1):
            res.append(base + i * cha)
        return res


# 方法3
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int):
        if k == 0:
            return []
        res = set()
        for i in range(k + 1):
            temp = shorter * i + longer * (k - i)
            res.add(temp)
        res = list(res)
        res.sort()
        return res



if __name__ == '__main__':
    s = Solution()
    shorter = 1
    longer = 1
    k = 100000
    print(s.divingBoard(shorter, longer, k))