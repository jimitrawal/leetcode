class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        b=len(height)-1
        area=0
        
        while a<=b:
            h=min(height[a],height[b])
            w=b-a
            niuarea=h*w        
            if niuarea>area:
                area=niuarea
            if height[b]>height[a]:
                a+=1
            else:
                b-=1
        return area