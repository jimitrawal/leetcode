class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        w=abs(l-r)
        h=min(height[l],height[r])
        area = h*w
        while l<r:
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
            w2=abs(l-r)
            h2=min(height[l],height[r])
            area2 = h2*w2
            if area2>area:
                area=area2
        return area