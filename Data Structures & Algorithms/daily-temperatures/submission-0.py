class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #stack[-1] iis top of stack while [0] is the temperature
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (index - stackIndex)
            stack.append([temp,index])
        return result
            
            #while temperatures
        