class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #loop though list and find element
       
        #binary search
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: #nums[mid] == target
                return mid
        return -1



        """
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
        """
        """
        What type of question? Search and find element. Binary Search.

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + right //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        """
        """
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return -1
        #for index,value in enumerate(nums):
        #    if value == target:
        #        return index
        #return -1
        """