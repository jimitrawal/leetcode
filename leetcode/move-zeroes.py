class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1:
            x = 0
            y = 1
            while y<len(nums):
                if nums[x]!=0:
                    x+=1
                if nums[x] == 0 and nums[y]!=0:
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp
                else:
                    y+=1