class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        product =1
        addition = 0
        while (temp != 0):
            last_digit = temp%10
            temp  = temp//10
            product *= last_digit
            addition += last_digit
        result = product - addition
        return result

