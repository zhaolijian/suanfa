# 判断一个数字是否是回文数字


# # 方法1： 每次对数字取余数
# def solution(number):
#     last = 0
#     l = number
#     while l > 0:
#         temp = l % 10
#         last = last * 10 + temp
#         l = l // 10
#     if last == number:
#         return True
#     else:
#         return False

# 方法2： 设置首尾指针, 复杂度为O(n)
def solution(number):
    start = 0
    end = len(number) - 1
    while start < end:
        if number[start] != number[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    numebr = input()
    print(solution(numebr))