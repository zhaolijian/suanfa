# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
# 请你实现 ParkingSystem 类：
# ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。
# 一辆车只能停在  carType 对应尺寸的停车位中。如果没有空车位，请返回 false ，否则将该车停入车位并返回 true 。


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.array = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.array[carType - 1] -= 1
        return True if self.array[carType - 1] >= 0 else False