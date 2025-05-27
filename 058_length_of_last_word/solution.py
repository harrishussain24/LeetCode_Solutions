class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trim = s.split(" ")
        i = 0
        while i < len(trim):
            if trim[i] == "":
                trim.pop(i)
            else:
                i += 1
        return len(trim[-1])