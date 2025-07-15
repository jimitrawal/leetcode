class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l] > nums[r] and nums[r-1] < nums[r]:
                r-=1
            elif nums[l] > nums[r] and nums[r-1] >= nums[r]:
                return nums[r]
            elif nums[l] < nums[r] and nums[l+1] < nums[l]:
                l+=1
            elif nums[l] < nums[r] and nums[l+1] >= nums[l]:
                return nums[l]