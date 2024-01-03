class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n-1):
            two, one = one, one+two

        return one
