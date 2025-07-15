class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        start = 1
        for i in range(2,n):
            
            if nums[start-1] != nums[i]:
                start += 1
                nums[start] = nums[i]
        return start+1
