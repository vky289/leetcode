class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1, r2 = 0,0
        for n in nums:
            r2, r1 = max(r1+n, r2), r2

        return r2
