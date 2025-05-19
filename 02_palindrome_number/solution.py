
# with converting int to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x) #Converting to String
        final = rev[::-1] #Reversing the String
        if(rev == final) : 
            return True
        else : 
            return False