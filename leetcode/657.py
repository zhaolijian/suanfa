# 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
# 移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
# 如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
# 注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。
# 此外，假设每次移动机器人的移动幅度相同。
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return True
        d = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
        x, y = 0, 0
        for i in range(len(moves)):
            remove_x, remove_y = d[moves[i]]
            x += remove_x
            y += remove_y
        return True if x == 0 and y == 0 else False