class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mt = []
        for i in range(len(nums1)):
            maximum = nums1[i]
            tag = False
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    tag = True
                if tag == True and nums2[j] > maximum:
                    maximum = nums2[j]
                    break
            if maximum == nums1[i]:
                mt.append(-1)
            else:
                mt.append(maximum)
        return mt