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
        left = 0
        right = len(heights) - 1
        area = 0
        store = []
        while left < right:
            area = min(heights[left],heights[right]) * (right+1 - (left+1))
            if right == left+1:
                left += 1
                right = len(heights) - 1
            else:
                right -= 1
            store.append(area)
        return max(store)
    
        