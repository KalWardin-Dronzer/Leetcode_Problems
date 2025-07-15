class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        add = 0
        for i in nums:
            add += i 
            output.append(add)

        return output
