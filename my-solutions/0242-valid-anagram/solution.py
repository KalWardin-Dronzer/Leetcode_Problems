class Solution:
    def freq(self, s:str):
        frequency = {}
        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        return frequency

    def isAnagram(self, s: str, t: str) -> bool:
        return self.freq(s)== self.freq(t)
