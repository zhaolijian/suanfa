class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        init = {}
        for ele in strs:
            keys = ''.join(sorted(ele))
            if keys not in init:
                init[keys] = [ele]
            else:
                init[keys].append(ele)
        return list(init.values())


