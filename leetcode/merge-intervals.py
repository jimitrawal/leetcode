class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort()
        i=0
        while i<len(intervals)-1:
            currH = intervals[i][0]
            currT = intervals[i][1]
            nextH = intervals[i+1][0]
            nextT = intervals[i+1][1]
            if currT>=nextH:
                if currH>nextH:
                    intervals[i]=[nextH,currT]
                elif currT>nextT:
                    intervals[i]=[currH,currT]                
                else:
                    intervals[i]=[currH,nextT]
                intervals.pop(i+1)
            else:  
                if i==len(intervals)-2:
                    break
                i+=1
        return intervals