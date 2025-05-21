class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        j = 0

        while True:
            if j >= len(strs[0]):
                break
            temp = strs[0][j]
            
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != temp:
                    return output
                    exit()
            
            output += temp
            j += 1
        return output