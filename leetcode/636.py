class Solution:
    def exclusiveTime(self, n: int, logs):
        res= [0 for i in range(n)]
        i = 1
        # 栈中最后一个元素开始时间
        pre_time = int(logs[0][-1])
        # stack中存放id
        stack = [int(logs[0][0])]
        length = len(logs)
        while i < length:
            cur = logs[i].split(':')
            id, single, time = int(cur[0]), cur[1], int(cur[2])
            if single == 'start':
                if stack:
                    res[stack[-1]] += time - pre_time
                pre_time = time
                stack.append(id)
            else:
                res[stack.pop()] += time - pre_time + 1
                pre_time = time + 1
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n = 1
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    print(s.exclusiveTime(n, logs))