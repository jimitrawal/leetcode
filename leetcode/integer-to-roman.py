class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
        n = num
        times = 0
        p = len(roman)-1
        mt = ""
        while n>0:
            if n>=roman[p][1]:
                if (str(n))[0]=="9" :
                    mt+=roman[p-1][0]
                    mt+=roman[p+1][0]
                    p-=1
                elif (str(n))[0]=="4":
                    mt+=roman[p][0]
                    mt+=roman[p+1][0]
                else:
                    times = n//roman[p][1]
                    for i in range(times):
                        mt+=roman[p][0]
                n=n%roman[p][1]
            else:
                p-=1
        return mt