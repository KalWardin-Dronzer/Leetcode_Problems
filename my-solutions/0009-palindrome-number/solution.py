class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes

        original = x
        rev_x = 0

        while x != 0:
            last_digit = x % 10
            rev_x = rev_x * 10 + last_digit
            x = x // 10

        return original == rev_x

