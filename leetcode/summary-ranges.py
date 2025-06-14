class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a=0
        b=0
        mt=[]
        while a<len(nums):
            if b==len(nums)-1:
                if a==b:
                    mt.append(str(nums[a]))
                else:
                    mt.append(str(nums[a]) + "->" + str(nums[b]))
                break
            elif nums[b]+1==nums[b+1]:
                b+=1
            else:
                if a==b:
                    mt.append(str(nums[a]))
                else:
                    mt.append(str(nums[a]) + "->" + str(nums[b]))
                b+=1
                a=b
        return mt