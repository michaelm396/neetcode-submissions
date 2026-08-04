class Solution:
    import heapq


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap and or priorty que question
        # given an array of numbers and k value, return k most frequent elemnts.
        # give a list of numbers. I need to understand what numbers repeat the most. Then k
        # represents which top k elements need to be returned. Like top 2 elements most repeted elements
        # use dictionary or heapq to store. loop through to store elements. key is elements, value is count
        # return list of top k most repeated elements []
        """
        1. Store list into dictionary along with count
        2. return the nlargest value in heapq
        """
        store = {}
        for num in nums:
            if num in store:
                val = store[num] + 1
                store[num] = val
            elif num not in store:
                store[num] = 1
        top_k_keys = heapq.nlargest(k, store, key=store.get)
        return top_k_keys
        """
        store = {}
        for num in nums:
            if num in store:
                count = store[num]
                count = count + 1
                store[num] = count
            elif num not in store:
                store[num] = 1
        top_k_keys = heapq.nlargest(k, store, key=store.get)
        return top_k_keys
        """
        """
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for freq, num in heap:
            result.append(num)
        return result
        """
