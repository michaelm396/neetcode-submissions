class Solution:
    # Create pointers to iterate through list
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in res]
        """
        res = []
        nums.sort()

        for i,value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                threesum = value + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+= 1
        return res
        
        