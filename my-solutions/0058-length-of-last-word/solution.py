class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        lw = words[-1]
        return len(lw)
