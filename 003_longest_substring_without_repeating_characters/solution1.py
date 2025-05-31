class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lists = []
        pos = []
        count = 0

        i = 0
        while i < len(s):
            if s[i] in lists:
                pos.append("".join(lists))
                idx = lists.index(s[i])
                lists = lists[idx+1:]
                lists.append(s[i])
            else:
                lists.append(s[i]) 
            i += 1

        if lists:
            pos.append("".join(lists))

        for s in pos:
            count = max(count, len(s))
        
        return count