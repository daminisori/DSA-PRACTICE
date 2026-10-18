
class Solution(object):
    def maxArea(self, height):
    
        i = 0
        j =len(height)-1
        max_area =0
        while i < j:
            k= min(height[i],height[j])
            area = k*(j-i)
            max_area = max(max_area,area)
            if height [i]< height[j]:
                i+=1
            else:
                j-=1
        return max_area        