# class Solution(object):
#     def letterCombinations(self, digits):
#         if not digits:
#             return []
#         d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         res = []
#
#         def dfs(tmp, index):
#             if index == len(digits):
#                 res.append(tmp)
#                 return
#             c = digits[index]
#             letters = d[ord(c) - 50]
#             for i in letters:
#                 dfs(tmp + i, index + 1)
#         dfs("", 0)
#         return res


# 队列
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		# 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
		# 这里也可以用map，用数组可以更节省点内存
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		# 先往队列中加入一个空字符
		res = [""]
		for i in digits:
			size = len(res)
			# 由当前遍历到的字符，取字典表中查找对应的字符串
			letters = d[ord(i)-48]
			# 计算出队列长度后，将队列中的每个元素挨个拿出来
			for _ in range(size):
				# 每次都从队列中拿出第一个元素
				tmp = res.pop(0)
				# 然后跟"def"这样的字符串拼接，并再次放到队列中
				for j in letters:
					res.append(tmp+j)
		return res


if __name__ == '__main__':
    s = Solution()
    digits = input()
    print(s.letterCombinations(digits))