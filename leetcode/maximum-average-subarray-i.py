class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        tot = 0
        maxtot = sum(nums[0:k])
        for end in range(len(nums)):
            tot += nums[end]
            if end-start == k-1:
                if tot > maxtot:
                    maxtot = tot
                
                tot-=nums[start]
                start+=1
                end=start-1
        return maxtot/k