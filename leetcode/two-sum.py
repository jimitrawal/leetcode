class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mt=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    mt.append(x)
                    mt.append(y)
        return mt