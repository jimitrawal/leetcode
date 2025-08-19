class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        if len(nums)==1:
            return nums[0]
        while i<len(nums)-1:
            if (nums[i] != (nums[i+1])):
                return nums[i]
            else:
                i+=2
        if i==len(nums)-1:
            return nums[i]