class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)

        maxi, mini = 1, 1

        for n in nums:
            maxi, mini = max(n, maxi*n, mini*n), min(n, maxi*n, mini*n)
            res = max(res, maxi)
        return res