class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            c = 0
            for j in nums:
                if j<i:
                    c += 1
            output.append(c)
        return output
