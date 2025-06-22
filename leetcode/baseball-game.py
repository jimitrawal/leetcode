class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mt=[]
        j=0
        for i in range(len(operations)):
            if operations[i]=="C":
                mt.pop(j-1)
                j-=1
            elif operations[i]=="D":
                mt.append(mt[j-1]*2)
                j+=1
            elif operations[i]=="+":
                if i>1:
                    mt.append(mt[j-1]+mt[j-2])
                else:
                    mt.append(mt[i-1])
                j+=1
            else:
                mt.append(int(operations[i]))
                j+=1
        return sum(mt)