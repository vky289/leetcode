class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0
        def find_palindrome(l, r):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

        for i in range(len(s)):
            l = r = i
            find_palindrome(l, r)
            l, r = i, i+1
            find_palindrome(l, r)

        return res
