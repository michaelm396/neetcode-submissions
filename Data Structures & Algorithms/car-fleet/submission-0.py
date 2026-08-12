class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(0,len(position)):
            pair.append([position[i],speed[i]])
        pair = sorted(pair)
        stack = []
        for positions,speeds in pair[::-1]:
            stack.append((target - positions) / speeds) # target 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
