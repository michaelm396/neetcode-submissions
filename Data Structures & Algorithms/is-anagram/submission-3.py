class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict1 = {}
        dict2 = {}
        for value in s:
            if value in dict1:
                sub = dict1[value]
                sub = sub + 1
                dict1[value] = sub
            if value not in dict1: 
                dict1[value] = 1
        
        for value in t:
            if value in dict2:
                sub = dict2[value]
                sub = sub + 1
                dict2[value] = sub
            if value not in dict2: 
                dict2[value] = 1
        print(dict1)
        print(dict2)
        if dict1 == dict2:
            return True
        else:
            return False