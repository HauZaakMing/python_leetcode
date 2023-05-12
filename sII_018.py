import math


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_tmp = "".join(ch.lower() for ch in s if ch.isalnum())
        return s_tmp==s_tmp[::-1]




s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")