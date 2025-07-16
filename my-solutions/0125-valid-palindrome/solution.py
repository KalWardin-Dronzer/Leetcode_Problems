class Solution:
    def isAlphaNum(self, s:str) -> bool:
        x = ord(s)
        if 48<= x <= 57 or 97<=x<=122 or 65<=x<=90:
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i=0
        j = len(s)-1
        while i<j:
            if not self.isAlphaNum(s[i]):
                i += 1
            elif not self.isAlphaNum(s[j]):
                j -= 1
            elif s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
