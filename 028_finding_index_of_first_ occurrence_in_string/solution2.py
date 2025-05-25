class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        inc = 0
        while inc <= len(haystack) - len(needle):
            checker = haystack[inc: inc + len(needle)]
            if checker == needle:
                return inc
            inc += 1
        return -1