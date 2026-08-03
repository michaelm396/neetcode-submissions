class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1) if length of input is 1 return list:
        # 2) Create dictionary of sorted element (key:value) ((sort):[value])
        # 3) Return array of all values in dicttionary
        storage = {}
        if len(strs) <= 1:
            return [strs]
        
        for value in strs:
            element = "".join(sorted(value))
            if element not in storage:
                storage[element] = [value]
            elif element in storage:
                val = storage[element]
                val.append(value)
                storage[element] = val

        placeholder = []
        for key,value in storage.items():
            placeholder.append(value)
        return placeholder



