class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # 1. loop through list and append product of splice of list
        # 2. return list
        # [0:0] + [1:4], [0:1] + [2:4], [0:2] + [3:4], [0:3] + [4:4]
        store = []
        for i in range(0,len(nums)):
            newlist =  nums[0:i] + nums[i+1:len(nums)]
            product = math.prod(newlist)
            store.append(product)
        return store