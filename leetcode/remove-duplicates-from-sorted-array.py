class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        k=len(set(nums))
        edge=0
        while j<len(nums)-2:
            if j>=k-1:
                nums[j+1]="_"
                j+=1
            elif nums[i]!=nums[j]:
                nums[j+1]=nums[i]
                j+=1
                i+=1
            else:
                i+=1
        return k