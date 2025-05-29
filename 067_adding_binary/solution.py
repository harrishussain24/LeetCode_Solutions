class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        output = ""
        firstLen = len(a)
        secLen = len(b)

        if firstLen > secLen:
            b = "0" * (firstLen - secLen) + b
        elif secLen > firstLen:
            a = "0" * (secLen - firstLen) + a


        itr = len(a) - 1
        while itr >= 0:
            total = int(a[itr]) + int(b[itr]) + carry
            result = total % 2
            carry = total // 2
            output = str(result) + output
    
            itr -= 1

        if carry != 0:
            output = str(carry) + output

        return output