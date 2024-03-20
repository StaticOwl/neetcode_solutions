def isPalindrome(self, s: str) -> bool:
        s="".join(c.lower() for c in s if c.isalpha() or c.isnumeric())
        return s == s[::-1]