class Solution:
    def isHappy(self, n: int) -> bool:
        sp = n
        fp = self.sum_of_square(n)

        while sp != fp and fp != 1:
            sp = self.sum_of_square(sp)
            fp = self.sum_of_square(self.sum_of_square(fp))

        if fp == 1:
            return True

        return False


    def sum_of_square(self, n):

        total_sum = 0

        while n > 0:
            d = n%10
            n = n//10
            total_sum += d ** 2

        return total_sum