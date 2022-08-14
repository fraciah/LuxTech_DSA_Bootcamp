#container with most water
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of 
the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that
the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
def maxArea(height):
        l = 0
        r = len(height) - 1
        area = 0
        
        for i in range(len(height)):
            if height[l] < height[r]:
                area = max(area, height[l] * (r - l))
                l += 1
            else:
                area = max(area, height[r] * (r - l))
                r -= 1
        return area
print(maxArea(height = [1,8,6,2,5,4,8,3,7]))