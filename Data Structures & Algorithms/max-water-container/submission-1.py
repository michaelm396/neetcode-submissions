class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #create two pointers
        #left = 0
        #right = len(heights) -1
        #max_count = area (l x w)
        #length = len(heights) - 1 
        # could do nested for loop or while loop until condition is meet like left at end of list
        # while left < right:
            # if condition:
            #    left += 1
            # else:
            #    right -=1
        # Two pointer problem
        # 1) Intialize right pointer and left pointer
        # 2) while left isnt the size of right pointer
        # 3)
        
    
        left = 0
        right = len(heights) - 1
        max_area = 0
        store = []
        while left < right:
            width = right - left
            current_area = min(heights[left], heights[right]) * width
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
        