class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x // 2
        ans = 0 

        if x <= 1:
            return x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                ans = mid
                break
            elif mid * mid < x:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1

        return ans
        