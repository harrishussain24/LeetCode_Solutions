
# without converting int to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        reversedNumber = 0
        while x > reversedNumber:
            reversedNumber = reversedNumber * 10 + x % 10 
            x //= 10
        return x == reversedNumber or x == reversedNumber // 10 