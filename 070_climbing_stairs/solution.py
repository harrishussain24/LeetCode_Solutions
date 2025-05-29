class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        i = 2
        while i <= n:
            c = a + b
            a = b
            b = c
    
            i += 1
    
        return b
        