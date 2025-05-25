class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        inc = 0
        found = False
        while inc < len(haystack):
            checker = haystack[inc: inc + len(needle)]
            if((inc + len(needle)) > len(haystack)):
                print("Limit Exceeded")
                return -1
            elif checker == needle:
                
                found = True
                return inc
            else:
                inc += 1

        if not found:
            return -1