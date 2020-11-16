# 找出无序数组中和为N的两个数


# 哈希表思想 和为target的两个数 复杂度n，用空间换时间
# def getRes_HashMap(nums, target):
#     nums.sort()
#     result = set()
#     for index, number in enumerate(nums):
#         if target-number in nums[index+1:]:
#             result.add((number, target-number))
#     return result


# 和为target的两个数并且乘积最小
# def getRes_HashMap(nums, target):
#     result = []
#     for index, number in enumerate(nums):
#         if target-number in nums[index+1:]:
#             if len(result) == 0:
#                 result.append(number)
#                 result.append(target-number)
#             elif number * (target-number) < result[0] * result[1]:
#                 result.clear()
#                 result.append(number)
#                 result.append(target-number)
#     return result

#
# 找到和为N的三个数
# def getRes_HashMap(nums, target):
#     result = set()
#     for i, n1 in enumerate(nums):
#         for j, n2 in enumerate(nums[i+1:]):
#             if target - n1 - n2 in nums[i+j+2:]:
#                 min_n = min(n1, n2, target-n1-n2)
#                 max_n = max(n1, n2, target-n1-n2)
#                 result.add((min_n, target-min_n-max_n, max_n))
#     return result


# 使用双指针, 复杂度nlogn(排序)+n（遍历）找到和为target的两个数
# def getRes_HashMap(nums, target):
#     result = set()
#     nums = sorted(nums)
#     min_index = 0
#     max_index = len(nums)-1
#     while min_index < max_index:
#         if nums[min_index] + nums[max_index] == target:
#             result.add((nums[min_index], nums[max_index]))
#             min_index += 1
#             max_index -= 1
#         elif nums[min_index] + nums[max_index] < target:
#             min_index += 1
#         else:
#             max_index -= 1
#     return sorted(list(result))


# # 使用双指针，找到和为target的三个数
# def getRes_HashMap(nums, target):
#     result = set()
#     nums.sort()
#     for i in range(len(nums) - 2):
#         min_index = i+1
#         max_index = len(nums) - 1
#         while min_index < max_index:
#             if nums[i] + nums[min_index] + nums[max_index] == target and (nums[i], nums[min_index], nums[max_index]) not in result:
#                 result.add((nums[i], nums[min_index], nums[max_index]))
#                 min_index += 1
#                 max_index -= 1
#             elif nums[i] + nums[min_index] + nums[max_index] < target:
#                 min_index += 1
#             elif nums[i] + nums[min_index] + nums[max_index] > target:
#                 max_index -= 1
#     return sorted(list(result))


# 使用双指针，找到和为target的四个数
# def getRes_HashMap(nums, target):
#     result = set()
#     nums.sort()
#     for i in range(len(nums) - 3):
#         for j in range(i + 1, len(nums) - 2):
#             min_index = j + 1
#             max_index = len(nums) - 1
#             while min_index < max_index:
#                 if nums[i] + nums[j] + nums[min_index] + nums[max_index] == target and (nums[i], nums[j], nums[min_index], nums[max_index]) not in result:
#                     result.add((nums[i], nums[j], nums[min_index], nums[max_index]))
#                     min_index += 1
#                     max_index -= 1
#                 elif nums[i] + nums[j] + nums[min_index] + nums[max_index] < target:
#                     min_index += 1
#                 elif nums[i] + nums[j] + nums[min_index] + nums[max_index] > target:
#                     max_index -= 1
#     return sorted(list(result))


def getRes_HashMap(nums, target):
    nums.sort()
    result = set()
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i+1:]):
            for m, n3 in enumerate(nums[i+j+2:]):
                if target-nums[i]-nums[i+j+1]-nums[i+j+m+2] in nums[i+j+m+3:]:
                    temp = sorted(list([nums[i], nums[i+j+1], nums[i+j+m+2], target-nums[i]-nums[i+j+1]-nums[i+j+m+2]]))
                    result.add((temp[0], temp[1], temp[2], temp[3]))
    return sorted(result)


if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    target = int(input())
    print(getRes_HashMap(nums, target))
