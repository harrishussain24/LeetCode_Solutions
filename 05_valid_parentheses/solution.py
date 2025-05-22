class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '{' : '}', '[' : ']'}
        checker = []
        final = False
        i = 0

        while i < len(s):
            print(s[i])
            if s[i] in dict:
                checker.append(s[i])
            else :
                if not checker:
                    final = False
                    break
                else:
                    last_pushed = checker.pop()
                    if (dict[last_pushed] == s[i]) :
                        final = True
                    else :
                        final = False
                        break
            i += 1
        if not checker: 
            return final
        else : 
            final = False
            return final