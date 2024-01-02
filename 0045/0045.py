class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_length = len(nums)
        f_jump, c_jump , jump, i = 0, 0, 0, 0
        if total_length > 1:
            while c_jump < total_length:
                if c_jump == total_length-1: break
                f_jump = max(f_jump, i + nums[i])
                if i == c_jump:
                    jump += 1
                    c_jump = f_jump
                i += 1

        return jump