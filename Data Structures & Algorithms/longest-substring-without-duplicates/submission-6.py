class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #loop through string elements
        #count if element currently in set. If currently in the set
        #if in set, and if value > value currently in set
            #store count, reset counter and reset set until done with
        """
        Given a string, find the longest substring without duplicate characters
        Sliding window problem - meaning well need to create a window that overfits the string and compares across the string
        Typically O(n)
        Brute force method
        """
        # 1. create a left side of window, set to store elements, and max_count
        # 2. loop through lenghth of string
        # 3. while right is inside of set
        # 4. 
        left = 0
        right = 0
        seen = set()
        maxc = 0
        for right in range(len(s)):
            while s[right] in seen: # if we encounter a variable already in store
                seen.remove(s[left]) # update window by removing left most
                left += 1
            seen.add(s[right])
            maxc = max(maxc,right - left + 1)
        return maxc
        """
        left = 0 # left side of window
        seen = set() #storage
        maxc = 0
        for right in range(len(s)): #right opens as we iterate
            while s[right] in seen: #if we enconuter a varible already in our storage
                seen.remove(s[left]) # we remove the left most variable from our window
                left += 1 #increment our left slider
            seen.add(s[right]) #otherwise we add to our right window
            maxc = max(maxc,right - left + 1) 
        return maxc
        """
        
        """
        storage = set()
        count = 0
        max_count = 0
        for value in s:
            if value in storage:
                if count > max_count:#check if count > max_count
                    max_count = count#set max_count to count
                    print(max_count)
                count = 0#reset count
                storage = set()#reset storage
                storage.add(value)
                print(storage)
            elif value not in storage:
                storage.add(value) # add to storage
                count = count + 1 # add to count
                if count > max_count:#check if count > max_count
                    max_count = count#set max_count to count
        return max_count
        """


