class Solution:
    def reverse(self, x: int) -> int:
        mt=""
        tag=False
        if x==0:
            return 0
        if x<0:
            tag=True
            x=x*-1
        while x>=1:
            mt+=str(x%10)
            x=x//10
        print(int(mt))
        if int(mt)>(2**31)-1:
            return 0
        if tag==True:
            return int(mt)-int(mt)-int(mt)
        return int(mt)