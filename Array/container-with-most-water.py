class Solution:
    def maxArea(self, height: List[int]) -> int:
        d=len(height)-1
        start=0
        end= d
        max_area=0
        while start<end:
            area = min(height[start],height[end])*d
            if area>max_area:
                max_area=area
            if height[start]>height[end]:
                end-=1
            else:
                start+=1
            d-=1
        return max_area
        
