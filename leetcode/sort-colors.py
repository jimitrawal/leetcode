class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy = None
        i=0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                dummy = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = dummy
                i=0
            else:
                i+=1