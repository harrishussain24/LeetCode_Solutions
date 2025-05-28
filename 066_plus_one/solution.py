class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out= ""
        final = []

        i = 0
        while i < len(digits):
            out = out + str(digits[i])
    
            i+=1

        out = int(out) + 1

        out = str(out)
        j = 0
        while j < len(out):
            final.append(int(out[j]))
    
            j+=1

        return final