class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(ch.lower() for ch in s if ch.isalnum())
        return s_clean == s_clean[::-1]