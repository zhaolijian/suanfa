from collections import defaultdict
if __name__ == '__main__':
    while True:
        try:
            # 节点、边数
            n, m = map(int, input().split())
            times = {}
            sons = defaultdict(list)
            for i in range(m):
                first, second, time = map(int, input().split())
                times[(first, second)] = time
                times[(second, first)] = time
                sons[first].append(second)
                sons[second].append(first)
            end_line = list(input().split())
            start, end = int(end_line[0]), int(end_line[1])
            start_month, temp = end_line[2].split('.')
            start_month = int(start_month)
            start_day, start_hour = temp.split('/')
            start_day = int(start_day)
            start_hour = int(start_hour)
            res = []
            visisted = set()
            visisted.add(start)

            def func(start, end, cur_time):
                if start == end:
                    res.append(cur_time)
                    return
                for son in sons[start]:
                    if son not in visisted:
                        visisted.add(son)
                        func(son, end, cur_time + times[(start, son)])
                        visisted.remove(son)

            func(start, end, 0)
            min_time = min(res)
            day, hour = min_time // 24, min_time % 24
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (hour + start_hour) >= 24:
                start_day += (hour + start_hour) // 24
                start_hour = (hour + start_hour) % 24
            print(str(start_month) + '.' + str(start_day + day) + '/' + str(start_hour))

        except:
            break