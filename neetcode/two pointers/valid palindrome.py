class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        input = ''.join(char.lower() for char in s if char.isalpha() or char.isdigit())
        return input == input[::-1]
