class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        result = ''
        carry = '0'
        for bit1, bit2 in zip(reversed(a), reversed(b)):
            if bit1 == bit2:
                result = carry + result
                carry = bit1
            else:
                if carry == '0':
                    result = '1' + result
                else:
                    result = '0' + result

        if carry == '1':
            result = carry + result

        return result
            

