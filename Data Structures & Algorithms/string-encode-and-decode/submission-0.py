class Solution:
    # design algorithm to encode a list of strings
    # input -> ["Hello","World"]
    # output -> ["Hello","World"]
    # could use ascii characters as a delimiter

    # could take the srting, shift by 1 using ascii 
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded = "".join(encoded+str(length)+"#"+word)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        #loop until we find string and delimeter #
        while i < len(s): # lopp through length of string
            j = i # set pointer j to i
            while s[j] != "#": # loop unit we find a "#"
                j += 1 # increment pointer by 1
            found_number = int(s[i:j]) # we found "#" so grab number
            result.append(s[j + 1:j + 1 + found_number])
            i = j + 1 + found_number
        return result


