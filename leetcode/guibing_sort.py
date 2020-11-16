class Solution:
    def guibing_sort(self, array):
        length = len(array)
        if length <= 1:
            return array
        mid = length // 2
        l_array = self.guibing_sort(array[:mid])
        r_array = self.guibing_sort(array[mid:])
        l, r = 0, 0
        res = []
        while l < len(l_array) and r < len(r_array):
            if l_array[l] < r_array[r]:
                res.append(l_array[l])
                l += 1
            else:
                res.append(r_array[r])
                r += 1
        if l_array[l:]:
            res += l_array[l:]
        if r_array[r:]:
            res += r_array[r:]
        return res


if __name__ == '__main__':
    s = Solution()
    array = [3,5,3,1,2,7]
    print(s.guibing_sort(array))