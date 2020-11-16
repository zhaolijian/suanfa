class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        def dfs(cur):
            for ele in rooms[cur]:
                if ele not in s:
                    s.add(ele)
                    dfs(ele)

        s = set()
        s.add(0)
        dfs(0)
        return len(list(s)) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    rooms = [[1],[2],[3],[]]
    print(s.canVisitAllRooms(rooms))