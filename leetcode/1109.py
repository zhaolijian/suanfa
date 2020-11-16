class Solution:
    def corpFlightBookings(self, bookings, n: int):
        result = [0] * n
        for start, end, value in bookings:
            result[start-1] += value
            if end < n:
                result[end] -= value
        for i in range(1, n):
            result[i] += result[i-1]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))