# class Solution:
#     def restoreIpAddresses(self, s: str):
#         segs = 4
#         ans = []
#         segments = [0] * segs
#
#         def dfs(segId, segStart):
#             if segId == segs:
#                 if segStart == len(s):
#                     ans.append('.'.join(str(seg) for seg in segments))
#                 return
#
#             if segStart == len(s):
#                 return
#
#             if s[segStart] == '0':
#                 segments[segId] = 0
#                 dfs(segId + 1, segStart + 1)
#
#             addr = 0
#             for i in range(segStart, len(s)):
#                 addr = addr * 10 + (ord(s[i]) - ord('0'))
#                 if 0 < addr <= 255:
#                     segments[segStart] = addr
#                     dfs(segId + 1, i + 1)
#                 else:
#                     break
#
#         dfs(0, 0)
#         return ans


class Solution:
    def restoreIpAddresses(self, s: str):
        segs = 4
        ans = []
        segments = [0] * segs

        def dfs(segId, segStart):
            if segId == segs:
                if segStart == len(s):
                    ans.append('.'.join(str(seg) for seg in segments))
                return

            if segStart == len(s):
                return

            if s[segStart] == '0':
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)

            addr = 0
            for i in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[i]) - ord('0'))
                if 0 < addr <= 255:
                    segments[segId] = addr
                    dfs(segId + 1, i + 1)
                else:
                    break

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    ss = Solution()
    s = "25525511135"
    print(ss.restoreIpAddresses(s))