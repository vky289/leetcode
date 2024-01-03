class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def find_palindrome(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l = r = i
            find_palindrome(l, r)
            l, r = i, i+1
            find_palindrome(l, r)

        return count
