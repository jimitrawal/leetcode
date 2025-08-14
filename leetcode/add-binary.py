class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = a[::-1]
        b = b[::-1]
        i=0
        res=""
        while i<min(len(b),len(a)):
            res+=str((int(a[i]) + int(b[i]) + carry)%2)
            carry = (int(a[i]) + int(b[i]) + carry)//2
            i+=1
        if i<len(a):
            while i<len(a):
                res+=str((int(a[i]) + carry)%2)
                carry = (int(a[i]) + carry)//2
                i+=1
        elif i<len(b):
            while i<len(b):
                res+=str((int(b[i]) + carry)%2)
                carry = (int(b[i]) + carry)//2
                i+=1
        if carry==1:
            res+=str(carry)
        return res[::-1]