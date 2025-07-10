class Solution:
    def countDigits(self, num: int) -> int:
        output = 0
        new_num = num
        while new_num!= 0:            
            digits = new_num % 10            
            if num%digits==0:
                output += 1
            new_num = new_num//10
        return output

