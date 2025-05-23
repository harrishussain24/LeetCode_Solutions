class Solution:
    def romanToInt(self, s: str) -> int:
        #creating Dictionary
        symbols = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900 }
        i = 0
        number = 0
        while i < len(s) :
            if( i+1 < len(s) and s[i:i+2]) in symbols :
                number += symbols[s[i:i+2]]
                i += 2
            else :
                number += symbols[s[i]]
                i += 1
        return number